import pytest

@pytest.fixture(scope = "session", autouse = True)
def tc_setup(browser):
    if browser == "chrome":
        print("Launch Chrome")
    else:
        print("Launch Browser")
    yield
    if browser == "chrome":
        print("Close Chrome")
    else:
        print("Close Browser")
@pytest.fixture(scope = "session", autouse = True)
def browser(request):
    return request.config.getoption("--browser")
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(params=["a","b"])
def param_setup(request):
    print (request.param)

