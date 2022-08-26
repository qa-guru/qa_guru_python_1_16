from uuid import uuid4

import requests


def test_add_to_cart_unauthorized():
    response = requests.post(
        'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': '788e4c44-c0ef-4f14-ab55-2faa7179bfcd;'}
    )
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_unauthorized_one_product():
    response = requests.post(
        'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': str(uuid4())}
    )
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert response.json()['updatetopcartsectionhtml'] == "(1)"


def test_add_to_cart_unauthorized_two_product():
    uid = str(uuid4())
    requests.post(
        'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': uid}
    )
    response = requests.post(
        'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': uid}
    )

    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_authorized():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    auth_cookie_name = 'NOPCOMMERCE.AUTH'
    login = os.getenv('user_login')
    password = os.getenv('user_password')
    response = requests.post(
        'https://demowebshop.tricentis.com/login',
        data={'Email': login, 'Password': password},
        allow_redirects=False
    )
    auth_cookie_value = response.cookies.get(auth_cookie_name)

    response = requests.post(
        'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
        cookies={auth_cookie_name: auth_cookie_value}
    )

    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert response.json()['updatetopcartsectionhtml'] == "(1)"
