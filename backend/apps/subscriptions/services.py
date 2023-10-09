from datetime import datetime

import stripe
import requests
import json
import os
import binascii

from django.conf import settings
from typing import NamedTuple, Optional

from .models import PayPalProduct, UserSubscription, Plan

from apps.users.models import User
from apps.users.services import get_user_by_id


class PayPalPaymentData(NamedTuple):
    instance: Optional[PayPalProduct] = None
    error: Optional[str] = None


class PayPalAuthMixin:

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


class PayPalService(PayPalAuthMixin):

    @property
    def products_url(self):
        return f'{self.urls_first_part}/v1/catalogs/products'

    @staticmethod
    def __generate_request_id():
        return binascii.hexlify(os.urandom(16)).decode()

    @property
    def headers_dict(self):
        request_id = self.__generate_request_id()
        headers_dict = {
            'Authorization': self.auth_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'PayPal-Request-Id': f'{request_id}',
            'Prefer': 'return=representation'
        }
        return headers_dict

    def create_product(self, product: PayPalProduct):
        data_for_post = {
            'name': product.name,
            'description': product.description,
            'type': 'SERVICE',
            'category': 'SOFTWARE',
            'image_url': product.image_url,
            'home_url': product.home_url
        }
        response = requests.post(
            self.products_url,
            headers=self.headers_dict,
            data=json.dumps(data_for_post)
        )
        product_id = response.json().get('id')
        product.product_id = product_id
        product.save()

    @property
    def current_product_data(self):
        try:
            product = PayPalProduct.objects.all()[:1].get()
        except PayPalProduct.DoesNotExist:
            return PayPalPaymentData(error='PayPal payment product does not exist!')
        return PayPalPaymentData(instance=product)

    def create_plan(self, data: dict) -> str | None:
        product_data = self.current_product_data

        if product_data.instance is None:
            return None
        product: PayPalProduct = product_data.instance

        data_for_post = {
            "product_id": product.product_id,
            "name": data['name'],
            "description": data['description'],
            "status": "ACTIVE",
            "billing_cycles": [
                {
                    "frequency": {
                        "interval_unit": "MONTH",
                        "interval_count": data['period_in_months']
                    },
                    "tenure_type": "TRIAL",
                    "sequence": 1,
                    "total_cycles": 2,
                    "pricing_scheme": {
                        "fixed_price": {
                            "value": data['price'],
                            "currency_code": "USD"
                        }
                    }
                },
                {
                    "frequency": {
                        "interval_unit": "MONTH",
                        "interval_count": data['period_in_months']
                    },
                    "tenure_type": "TRIAL",
                    "sequence": 2,
                    "total_cycles": 3,
                    "pricing_scheme": {
                        "fixed_price": {
                            "value": data['price'],
                            "currency_code": "USD"
                        }
                    }
                },
                {
                    "frequency": {
                        "interval_unit": "MONTH",
                        "interval_count": data['period_in_months']
                    },
                    "tenure_type": "REGULAR",
                    "sequence": 3,
                    "total_cycles": 12,
                    "pricing_scheme": {
                        "fixed_price": {
                            "value": data['price'],
                            "currency_code": "USD"
                        }
                    }
                }
            ],
            "payment_preferences": {
                "auto_bill_outstanding": True,
                "setup_fee": {
                    "value": "0",
                    "currency_code": "USD"
                },
                "setup_fee_failure_action": "CONTINUE",
                "payment_failure_threshold": 3
            },
            "taxes": {
                "percentage": "10",
                "inclusive": False
            }
        }
        response = requests.post(
            f'{self.urls_first_part}/v1/billing/plans',
            headers=self.headers_dict,
            data=json.dumps(data_for_post)
        )
        return response.json().get('id')

    @staticmethod
    def __check_values_keys(value, allowed_keys):
        value_dict = {}
        for k, v in value.items():
            if k in allowed_keys:
                value_dict[k] = v
        return value_dict

    def __subscription_detail_response(self, response: dict) -> dict:
        allowed_keys = ('id', 'plan_id', 'start_time', 'links',
                        'billing_info', 'next_billing_time',
                        'failed_payments_count', 'status')
        response_data = {}
        for key, value in response.items():
            if key in allowed_keys:
                if isinstance(value, dict):
                    value = self.__check_values_keys(value, allowed_keys)
                response_data[key] = value
        return response_data

    def get_subscription_by_id(self, subscription_id) -> dict:
        url = f'{self.urls_first_part}/v1/billing/subscriptions/{subscription_id}'
        response = requests.get(url, headers=self.headers_dict).json()
        data = self.__subscription_detail_response(response)
        response_data = {
            'subscription_id': data.get('id'),
            'plan_id': data.get('plan_id'),
            'start_time': data.get('start_time'),
            'cancel_link': data.get('links')[0]['href'],
            'next_pay_time': data.get('billing_info').get('next_billing_time'),
            'failed_payments_count': data.get('billing_info').get('failed_payments_count'),
            'status': data.get('status')
        }
        return response_data

    @staticmethod
    def get_user_subscription_from_db(subscription_pk) -> UserSubscription | None:
        if not UserSubscription.objects.filter(id=subscription_pk).exists():
            return None
        return UserSubscription.objects.get(id=subscription_pk)

    @staticmethod
    def get_plan_by_pp_id(plan_id) -> Plan | None:
        if not Plan.objects.filter(paypal_plan_id=plan_id).exists():
            return None
        return Plan.objects.get(paypal_plan_id=plan_id)

    def create_user_subscription(self, user: User, subscription_id):
        pp_subscription_data = self.get_subscription_by_id(subscription_id)

        plan_id = pp_subscription_data.get('plan_id')
        plan = self.get_plan_by_pp_id(plan_id)

        if pp_subscription_data['status'] == 'ACTIVE':
            subscription, _ = UserSubscription.objects.get_or_create(
                plan=plan,
                user=user,
                start_time=pp_subscription_data['start_time'],
                next_pay_time=pp_subscription_data['next_pay_time'],
                payment_service=1,  # PAYPAL,
                status=pp_subscription_data['status'],
                paypal_subscription_cancel_link=pp_subscription_data['cancel_link'],
                paypal_subscription_id=subscription_id
            )
            return subscription
        return None

    def cancel_subscription(self, subscription_pk) -> bool:
        subscription = self.get_user_subscription_from_db(subscription_pk)

        if subscription is not None:
            headers = {
                'Authorization': self.auth_token,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            data = {'reason': 'Not satisfied with the service'}
            response = requests.post(
                subscription.paypal_subscription_cancel_link,
                headers=headers,
                data=json.dumps(data)
            )
            if not response.status_code == 204:
                return False
            subscription.status = 'CANCELED'
            subscription.save()
            return True
        return False


class StripeAPIMixin:

    @staticmethod
    def configure_stripe():
        stripe.api_key = settings.STRIPE_SECRET_KEY

    def create_price(self, data, stripe_product_id):
        self.configure_stripe()
        price = stripe.Price.create(
            unit_amount=data['price'],
            currency="usd",
            recurring={
                "interval": "month",
                "interval_count": data['interval']
            },
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


class StripeMixin(StripeAPIMixin):

    @property
    def webhook_url(self):
        return settings.STRIPE_ENDPOINT_SECRET

    def create_checkout_session(
            self,
            client_id,
            plan: Plan
    ):
        self.configure_stripe()
        checkout_session = stripe.checkout.Session.create(
            client_reference_id=client_id,
            success_url=settings.STRIPE_SUCCESS_URL,
            cancel_url=settings.STRIPE_CANCEL_URL,
            payment_method_types=['card'],
            mode='subscription',
            line_items=[
                {
                    'price': plan.stripe_price_id,
                    'quantity': 1,
                }
            ]
        )

        session_id = checkout_session.get('id')
        return session_id

    def get_stripe_subscription_data(self, payload, sig_header):
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
            stripe_subscription_id = session.get('subscription')

            sub_detail = stripe.Subscription.retrieve(
                stripe_subscription_id
            )
            return {
                'user_id': client_reference_id,
                'subscription_id': stripe_subscription_id,
                'plan_price_id': sub_detail['items'].get('data')[0].get('price')['id'],
                'start_time': datetime.fromtimestamp(sub_detail['current_period_start']),
                'next_pay_time': datetime.fromtimestamp(sub_detail['current_period_end'])
            }
        return None

    def create_user_subscription(self, payload, sig_header) -> bool:
        self.configure_stripe()
        sub_data = self.get_stripe_subscription_data(payload, sig_header)

        if sub_data is None:
            return False

        user = get_user_by_id(sub_data.get('user_id'))

        if user is not None:
            try:
                plan = Plan.objects.get(stripe_price_id=sub_data['plan_price_id'])
            except (Exception,):
                return False

            UserSubscription.objects.create(
                plan=plan,
                user=user,
                start_time=sub_data['start_time'],
                next_pay_time=sub_data['next_pay_time'],
                stripe_subscription_id=sub_data['subscription_id'],
                status='ACTIVE',
                payment_service=2
            )
            return True
        return False

    def cancel_subscription(self, sub_pk) -> bool:
        try:
            user_sub = UserSubscription.objects.get(id=sub_pk)
        except (Exception,):
            return False
        self.configure_stripe()

        if user_sub.stripe_subscription_id is None:
            return False

        response = stripe.Subscription.delete(
            user_sub.stripe_subscription_id
        )
        if response.get('status') == 'canceled':
            user_sub.status = 'CANCELED'
            user_sub.save()
        else:
            return False
        return True


class PaymentService:
    paypal = PayPalService()
    stripe = StripeMixin()


class UserSubscriptionsService:

    @staticmethod
    def get_plan_by_pk(plan_pk):
        if Plan.objects.filter(id=plan_pk).exists():
            return Plan.objects.get(id=plan_pk)
        return None

    @staticmethod
    def user_have_active_subscriptions(user: User) -> bool:
        if user.subscriptions.filter(status='ACTIVE').exists():
            return True
        return False

    @staticmethod
    def get_active_subscription(user_pk):
        """
        If user have more than one active
        subscription, method will return None.
        In the other case, it will return
        user subscription instance.
        """
        user = get_user_by_id(user_pk)
        if user is None:
            return None

        user_active_subs = user.subscriptions.filter(status='ACTIVE')

        if user_active_subs.exists() and user_active_subs.count() == 1:
            subscription = user.subscriptions.get(status='ACTIVE')
            return subscription
        return None
