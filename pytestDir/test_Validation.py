import pytest


@pytest.fixture(scope="function")
def secondWork():
    print("I setup second world statement")  #before test it will execute
    yield
    print("I am teardown validation")  #after test this will get execute

@pytest.mark.skip #to skip a test
def test_initialCheck(prework, secondWork):
    print("This is the first testCase there")
    assert prework == "pass"


def test_second(prework, secondWork):
    print("This is the second Second testCase")
