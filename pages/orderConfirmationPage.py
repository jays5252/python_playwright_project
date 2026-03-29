from playwright.sync_api import Page

class OrderConfirmationPage:
    def __init__(self, page:Page):
        self.page = page
        self.confirmationMessage = self.page.locator(".hero-primary")
        self.orderId = self.page.locator("td label.ng-star-inserted")
        self.historypageLink = self.page.locator('label[routerlink="/dashboard/myorders"]')

    def getOrderid(self):
        wordsmiths =  self.orderId.text_content()
        orderId = wordsmiths.strip().split(" ")[1]
        return orderId

    def navigateToOrderHistory(self):
        self.historypageLink.click()