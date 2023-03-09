import pytest
from dotenv import load_dotenv

from framework.demoqa_with_env import DemoQaWithEnv


load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env")


@pytest.fixture(scope="session")
def demoshop(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def auth_user(env):
    return DemoQaWithEnv(env).demoqa


@pytest.fixture(scope="session")
def regres_api(env):
    return DemoQaWithEnv(env).reqres
