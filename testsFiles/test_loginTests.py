import json

import pytest
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage

with open('test_data/credentials.json') as credsData:
    testdata = json.load(credsData)
    userCredentialsList = testdata["credentials"]

@pytest.mark.parametrize('user_credentials',userCredentialsList)
def test_login_with_validCredentials(page:Page, user_credentials):
    loginpage = LoginPage(page)
    loginpage.navigateToLoginPage("https://rahulshettyacademy.com/client")
    loginpage.login(user_credentials["username"],user_credentials["password"])
    expect(page).to_have_title("Let's Shop")

def test_login_with_invalidCredentials(page:Page, user_credentials):
    loginpage = LoginPage(page)
    loginpage.navigateToLoginPage("https://rahulshettyacademy.com/client")
    loginpage.login(user_credentials["username"],"User@123")
    expect(loginpage.errorMassage).to_be_visible()
    expect(loginpage.errorMassage.text_content()).tobe("")