from typing import NamedTuple, Optional

import stripe
import requests
import json

from django.conf import settings

from .models import PayPalProduct


class PayPalPaymentData(NamedTuple):
    instance: Optional[PayPalProduct] = None
    error: Optional[str] = None


class PayPalAuthMixin:

    @staticmethod
    def get_access_token() -> str | None:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }
        auth = (settings.PAYPAL_CLIENT_ID, settings.PAYPAL_SECRET)
        url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
        response = requests.post(url, headers=headers, data=data, auth=auth)
        print(response.json())
        return response.json().get('access_token')

    @property
    def auth_token(self):
        return f'Bearer {PayPalAuthMixin.get_access_token()}'


class PayPalService(PayPalAuthMixin):

    @property
    def products_url(self):
        return 'https://api-m.sandbox.paypal.com/v1/catalogs/products'

    @property
    def headers_dict(self):
        headers_dict = {
            'Authorization': self.auth_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'PayPal-Request-Id': 'PRODUCT-23231-001',
            'Prefer': 'return=representation'
        }
        return headers_dict

    def create_product(self, data: dict) -> PayPalProduct:
        data_for_post = {
            'name': data['name'],
            'description': data['description'],
            'type': 'SERVICE',
            'category': 'SOFTWARE',
            'image_url': data['image_url'],
            'home_url': data['home_url']
        }
        response = requests.post(
            self.products_url,
            headers=self.headers_dict,
            data=json.dumps(data_for_post)
        )
        product_id = response.json().get('id')
        data['product_id'] = product_id

        product, _ = PayPalProduct.objects.get_or_create(
            **data
        )
        return product

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
                    "value": "10",
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
            'https://api-m.sandbox.paypal.com/v1/billing/plans',
            headers=self.headers_dict,
            data=json.dumps(data_for_post)
        )

        if response.status_code == 201:
            return response.json().get('id')
        return None


class StripeMixin:

    def create_checkout_session(
            self,
            success_url=None,
            cancel_url=None
    ):
        pass
