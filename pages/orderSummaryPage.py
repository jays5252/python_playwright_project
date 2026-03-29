from playwright.sync_api import Page

class OrderSummaryPage:
    def __init__(self, page:Page):
        self.page = page
        self.billingAddressSection= self.page.locator("div.address").nth(0)
        self.country = self.billingAddressSection.locator("p").nth(1)
        self.email= self.billingAddressSection.locator("p").nth(0)
        self.productName = self.page.locator('.title')
        self.orderid= self.page.locator('.-main')

    def getCountryFromOrder(self):
        mixedCountry = self.country.text_content()
        countryName =  mixedCountry.split("-")[1].lstrip()
        return countryName

    def getOrderIdFromOrder(self):
        orderId = self.orderid.text_content()
        return orderId

    def getProductName(self):
        productName = self.productName.text_content().strip()
        return productName

    def getEmailFromOrder(self):
        userEmail = self.email.text_content().strip()
        return userEmail