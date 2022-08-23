import os

import pytest
import requests
from allure import step, tag
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser


@pytest.fixture(autouse=True, scope='session')
def environment():
    load_dotenv()


LOGIN = os.getenv('user_login')
PASSWORD = os.getenv('user_password')
API_URL = os.getenv('api_url')
WEB_URL = os.getenv('web_url')
browser.config.base_url = WEB_URL


@tag("demowebshop")
def test_login():
    """Successful authorization to some demowebshop (UI)"""
    with step("Open login page"):
        browser.open("/login")

    with step("Fill login form"):
        browser.element("#Email").send_keys(LOGIN)
        browser.element("#Password").send_keys(PASSWORD).press_enter()

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))


@tag("demowebshop")
def test_login_with_cookie():
    """Successful authorization to some demowebshop (API + UI)"""
    with step("Get cookie by api and set it to browser"):
        authorization_cookie = requests.post(
            url=API_URL + '/login',
            params={'Email': LOGIN, "Password": PASSWORD},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )
        # assert authorization_cookie.status_code == 302
        authorization_cookie = authorization_cookie.cookies.get("NOPCOMMERCE.AUTH")
        print(authorization_cookie)

        with step("Open minimal content, because cookie can be set when site is opened"):
            browser.open("/Themes/DefaultClean/Content/images/logo.png")

        with step("Set cookie to to browser"):
            browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
        with step("Open main page"):
            browser.open("")
        with step("Verify successful authorization"):
            browser.element(".account").should(have.text(LOGIN))
