import os
from uuid import uuid4
from framework.demoqa import DemoQA, Cart
from utils.sessions import demoqa


def test_add_to_cart_unauthorized():
    response = DemoQA().add_to_cart()

    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_unauthorized_one_product():
    response = DemoQA().add_to_cart()

    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert response.json()['updatetopcartsectionhtml'] == "(1)"


def test_add_to_cart_unauthorized_two_product(unauthorized_customer):
    DemoQA().add_to_cart(cookies=unauthorized_customer)
    response = DemoQA().add_to_cart(cookies=unauthorized_customer)
    cart = Cart(response.json())

    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert cart.cart_product_count == '(2)'


def test_add_to_cart_authorized(demoqa_authorized):
    response = demoqa_authorized.post(
        '/addproducttocart/catalog/31/1/1',
    )

    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
