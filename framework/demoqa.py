import os
from requests import Response
from utils.requests_helper import BaseSession


class Cart:
    def __init__(self, json):
        self.json = json

    @property
    def cart_product_count(self):
        return self.json['updatetopcartsectionhtml']


class DemoQA:
    def __init__(self):
        self.demoqa = BaseSession(base_url=os.getenv('demo_shop_url'))

    def login(self, user, password, **kwargs):
        return self.demoqa.post(
            '/login',
            data={'Email': user, 'Password': password},
            allow_redirects=False
        )

    def add_to_cart(self, **kwargs) -> Response:
        cookies = kwargs.pop('cookies', None)
        result = self.demoqa.post('/addproducttocart/catalog/31/1/1', cookies=cookies)
        return result

