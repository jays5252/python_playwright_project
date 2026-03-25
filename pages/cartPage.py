from playwright.sync_api import Page

class CartPage:
    def __init__(self, page:Page):
        self.page = page
        self.productNameInCart = self.page.locator(".infoWrap h3").nth(0)
        self.checkOutButton = self.page.get_by_role("button", name="Checkout")

    def navigateToCheckOut(self):
        self.checkOutButton.click()