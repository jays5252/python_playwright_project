import pytest

#It will run before test suites
@pytest.fixture(scope="session")
def preSetup():
    print("I'm setup browser instance")
    return "pass"

#it will run before all class lavel excecution
@pytest.fixture(scope="class")
def preClass():
    print("I will get run once per my entire class")

#I will run before all tests
@pytest.fixture(scope="module")
def preModule():
    print("I will run before all tests")

#Will run before each test
@pytest.fixture(scope="function")
def prework():
    print("I'm setup browser instance")