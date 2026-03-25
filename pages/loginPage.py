from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.usernameField =self.page.locator("#userEmail")
        self.passwordField =self.page.locator("#userPassword")
        self.loginBtn =self.page.locator("#login")
        self.errorMassage = self.page.locator("#toast-container")

    def navigateToLoginPage(self, url: str) -> None:
        self.page.goto(url)

    def login(self, username:str, password:str):
        self.usernameField.fill(username)
        self.passwordField.fill(password)
        self.loginBtn.click()