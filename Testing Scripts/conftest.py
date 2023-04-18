import pytest

@pytest.fixture(scope = "session", autouse = True)
def tc_setup():
    print("Launch Browser")
    yield
    print("Close Browser")