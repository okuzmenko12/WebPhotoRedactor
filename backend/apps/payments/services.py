import json
import stripe

import requests
import binascii
import os

from typing import NamedTuple, Optional

from .models import Plan, Order, ForeignOrder

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from apps.users.services import get_user_by_id
from .utils import get_random_password, get_price_in_cents
from apps.users.models import User


class PaymentData(NamedTuple):
    data: Optional[dict] = None
    error: Optional[str] = None


class ForeignOrderData(NamedTuple):
    success: bool
    order_data: Optional[dict] = None
    message: Optional[str] = None


class QuerySetMixin:

    @staticmethod
    def get_model_instance_by_id(
            model,
            obj_id
    ):
        try:
            instance = model.objects.get(**{'id': obj_id})
        except (Exception,):
            return None
        return instance

    @staticmethod
    def create_instance_by_data(
            model,
            data: dict
    ) -> bool:
        try:
            model.objects.create(**data)
        except (Exception,):
            return False
        return True

    @staticmethod
    def get_instance_by_data(
            model,
            data: dict
    ):
        try:
            instance = model.objects.get(**data)
        except (Exception,):
            return None
        return instance


class OrderMixin(QuerySetMixin):
    foreign_order = False

    @property
    def model(self):
        model = Order
        if self.foreign_order:
            model = ForeignOrder
        return model

    def create_order_in_db(self, data):
        order = self.create_instance_by_data(self.model, data)
        return order

    def get_order_by_data(
            self,
            data
    ):
        model = Order
        instance = self.get_instance_by_data(model, data)
        if instance is None:
            model = ForeignOrder
            return self.get_instance_by_data(model, data)
        return instance

    @staticmethod
    def give_credits_to_order_user(
            order: Order
    ):
        user = order.user
        plan = order.plan
        counter_of_usage = user.counter_of_usage

        plan_credit_fields = [
            'up_scales_count',
            'bg_deletions_count',
            'jpg_artifacts_deletions_count'
        ]
        for field in plan_credit_fields:
            plan_field_value = getattr(plan, field)
            user_field_value = getattr(counter_of_usage, field)
            new_value = user_field_value + plan_field_value
            setattr(counter_of_usage, field, new_value)
        counter_of_usage.save()

    def complete_order(
            self,
            order: Order,
    ):

        order.status = 'COMPLETED'
        order.save()
        self.give_credits_to_order_user(order)  # give credits to customer


class PayPalContextMixin(OrderMixin):

    @property
    def urls_first_part(self):
        if not settings.PAYPAL_SANDBOX_URLS:
            return 'https://api-m.paypal.com'
        return 'https://api-m.sandbox.paypal.com'

    def get_access_token(self) -> str | None:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }
        auth = (settings.PAYPAL_CLIENT_ID, settings.PAYPAL_SECRET)
        url = f"{self.urls_first_part}/v1/oauth2/token"
        response = requests.post(url, headers=headers, data=data, auth=auth)
        return response.json().get('access_token')

    @property
    def auth_token(self):
        return f'Bearer {self.get_access_token()}'

    @staticmethod
    def generate_token_id():
        return binascii.hexlify(os.urandom(16)).decode()

    @property
    def headers_dict(self):
        headers_dict = {
            'Authorization': self.auth_token,
            'Content-Type': 'application/json',
            'PayPal-Request-Id': self.generate_token_id()
        }
        return headers_dict

    @property
    def order_creation_url(self):
        return 'https://api-m.sandbox.paypal.com/v2/checkout/orders'

    @staticmethod
    def get_capture_order_url(order_id):
        url = f'https://api-m.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture'
        return url


class PayPalOrdersMixin(PayPalContextMixin):

    def get_json_order_creation_data(
            self,
            **kwargs
    ):
        amount = kwargs.get('amount')
        success_url = kwargs.get('success_url')
        cancel_url = kwargs.get('cancel_url')

        data = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "reference_id": self.generate_token_id(),
                    "amount": {
                        "currency_code": "USD",
                        "value": str(amount)
                    }
                }
            ],
            "payment_source": {
                "paypal": {
                    "experience_context": {
                        "brand_name": "FlexFI Upscale",
                        "locale": "en-US",
                        "landing_page": "LOGIN",
                        "shipping_preference": "NO_SHIPPING",
                        "user_action": "CONTINUE",
                        "return_url": success_url if success_url is not None else settings.PAYMENT_SUCCESS_URL,
                        "cancel_url": cancel_url if cancel_url is not None else settings.PAYMENT_CANCEL_URL
                    }
                }
            }
        }
        return json.dumps(data)

    @staticmethod
    def order_create_response(response: requests.Response):
        if response.status_code != 200:
            return PaymentData(error='Something went wrong... Please, try again later.')

        resp_json_data: dict = response.json()
        order_id = resp_json_data.get('id')

        if order_id is None:
            return PaymentData(error='The order wasn\'t created. Please, try again.')  # noqa

        links = resp_json_data.get('links')
        if links is not None:
            payment_link = links[1]['href']
        else:
            return PaymentData(
                error='Something went wrong when creating the payment link. Please, try again.'
            )
        data = {
            'order_id': order_id,
            'payment_link': payment_link
        }
        return PaymentData(data=data)

    @staticmethod
    def capture_order_response(response: requests.Response):
        data: dict = response.json()
        status = data.get('status')
        if status != 'COMPLETED':
            return PaymentData(
                error='This payment wasn\'t successful! Please, try again.'  # noqa
            )

        return PaymentData(data={
            'order_id': data.get('id'),
            'status': status,
            'create_time': data.get('create_time')
        })

    def get_data_from_response(
            self,
            response: requests.Response,
            order_create=False,
            capture_order=False
    ):
        if order_create:
            return self.order_create_response(response)
        elif capture_order:
            return self.capture_order_response(response)
        return None

    def create_order(
            self,
            amount: int,
            success_url: str = None,
            cancel_url: str = None
    ) -> PaymentData | None:
        header = self.headers_dict
        json_data = self.get_json_order_creation_data(
            amount=amount,
            success_url=success_url,
            cancel_url=cancel_url
        )
        response = requests.post(
            self.order_creation_url,
            headers=header,
            data=json_data
        )
        return self.get_data_from_response(response, order_create=True)

    def capture_order(self, order_id):
        response = requests.post(
            self.get_capture_order_url(order_id),
            headers=self.headers_dict
        )
        return self.get_data_from_response(response, capture_order=True)


class StripePaymentMixin(OrderMixin):

    @staticmethod
    def configure_stripe():
        stripe.api_key = settings.STRIPE_SECRET_KEY

    @property
    def webhook_url(self):
        return settings.STRIPE_ENDPOINT_SECRET

    def create_price(self, data, stripe_product_id):
        self.configure_stripe()
        price = stripe.Price.create(
            unit_amount=data['price'],
            currency="usd",
            product=stripe_product_id,
        )
        return price

    @staticmethod
    def get_product_with_price_id(stripe_product_id, price_obj_id):
        stripe.Product.modify(
            stripe_product_id,
            default_price=price_obj_id,
        )
        return stripe.Product.retrieve(stripe_product_id)

    def create_product(self, data) -> str | None:
        self.configure_stripe()
        try:
            product = stripe.Product.create(
                name=data['name'],
                description=data['description']
            )
            price_obj = self.create_price(data, product.id)
            final_product = self.get_product_with_price_id(product.id, price_obj.id)
            return final_product.default_price
        except (Exception,):
            return None

    def create_checkout_session(
            self,
            client_id,
            plan: Plan = None,
            foreign_order: ForeignOrder = None,
    ):
        self.configure_stripe()

        success_url = settings.PAYMENT_SUCCESS_URL
        cancel_url = settings.PAYMENT_CANCEL_URL

        if foreign_order is not None:
            stripe_price_id = self.create_product({
                'name': f'Order #{foreign_order.ext_id}',
                'description': foreign_order.description if foreign_order.description is not None else '',
                'price': get_price_in_cents(foreign_order.amount)
            })
            success_url = foreign_order.success_url
            cancel_url = foreign_order.cancel_url

        else:
            stripe_price_id = plan.stripe_price_id
        checkout_session = stripe.checkout.Session.create(
            client_reference_id=client_id,
            success_url=success_url,
            cancel_url=cancel_url,
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'price': stripe_price_id,
                    'quantity': 1,
                }
            ]
        )
        session_id = checkout_session.get('id')

        if foreign_order is None:
            self.create_order_in_db({
                'plan': plan,
                'user': get_user_by_id(client_id),
                'status': 'ACTIVE',
                'payment_service': 'STRIPE',
                'stripe_session_id': session_id
            })
        else:
            foreign_order.stripe_session_id = session_id
            foreign_order.save()
        return session_id

    def complete_payment(self, payload, sig_header):
        self.configure_stripe()
        endpoint_secret = self.webhook_url

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except (Exception,):
            return None

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            client_reference_id = session.get('client_reference_id')

            data = {
                'stripe_session_id': session.get('id')
            }
            order: Order | ForeignOrder = self.get_order_by_data(data)

            if isinstance(order, Order):
                self.complete_order(order)
            else:
                print(order)

        return None


class UserCreateForPaymentMixin:
    mail_with_celery = True

    @classmethod
    def check_email_unique(cls, email: str) -> bool:
        if User.objects.filter(email=email).exists():
            return False
        return True

    @classmethod
    def get_random_password(cls):
        return get_random_password()

    @classmethod
    def get_html_email_for_data(cls, data: dict):
        context = {
            'email': data['email'],
            'password': data['password'],
            'full_name': data.get('full_name'),
            'website': settings.FRONTEND_DOMAIN
        }

        html_msg = render_to_string(
            'payments/create_user_for_sub_mail.html',
            context
        )
        return html_msg

    def create_user_for_email(self, email: str, full_name: str) -> User | None:
        try:
            user = User.objects.create(
                email=email,
                is_active=True,
                full_name=full_name
            )
            random_password = self.get_random_password()

            if self.mail_with_celery:
                pass
            else:
                send_mail(
                    subject='You successfully registered at FlexFi.',
                    message='',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                    html_message=self.get_html_email_for_data(data={
                        'email': email,
                        'password': random_password,
                        'full_name': full_name
                    })
                )

            user.set_password(random_password)
            user.save()
        except Exception as e:
            print(e)
            user = None
        return user


class ForeignOrderMixin(PayPalOrdersMixin):

    def foreign_paypal_capture(
            self,
            order_id
    ):
        order: ForeignOrder = self.get_order_by_data({'paypal_order_id': order_id})
        if order is None:
            return PaymentData(error='No such order with provided order ID')
        if order.is_ended:
            return PaymentData(error='This order is already ended!')

        data, error = self.capture_order(order_id)

        notify_data = {
            'success': True
        }
        if error is not None:
            notify_data['success'] = False
            notify_data['message'] = error
            self.notify(order, notify_data)
            return PaymentData(error='Payment error.')
        self.notify(order, notify_data)
        self.make_order_ended(order)
        return PaymentData(data={
            'success': 'Successful payment.'
        })

    @staticmethod
    def notify(
            order: ForeignOrder,
            data: dict
    ):
        data.update({
            'ext_id': order.ext_id,
            'amount': order.amount,
            'currency': order.currency
        })
        # requests.post(order.notify_url, data=json.dumps(data))

    @staticmethod
    def make_order_ended(order: ForeignOrder):
        order.is_ended = True
        order.save()
