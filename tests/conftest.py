import os

import allure
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from framework.demoqa_with_env import DemoQaWithEnv


load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def demoshop(env):
    return DemoQaWithEnv(env)


@pytest.fixture(scope="session")
def regres_api(env):
    return DemoQaWithEnv(env).reqres


@pytest.fixture(scope='session')
def cookie(demoshop):
    response = demoshop.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    return authorization_cookie


@pytest.fixture(scope='function')
def auth_user(demoshop, cookie):
    browser.config.base_url = demoshop.demoqa.url
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    yield browser
    browser.quit()
