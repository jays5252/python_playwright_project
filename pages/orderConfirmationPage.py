from playwright.sync_api import Page

class OrderConfirmationPage:
    def __init__(self, page:Page):
        self.page = page
        self.confirmationMessage = self.page.locator(".hero-primary")
        self.orderId = self.page.locator("td label.ng-star-inserted")

    def getOrderid(self):
        wordsmiths =  self.orderId.text_content()
        orderId = wordsmiths.split(" ")[1]
        return orderId