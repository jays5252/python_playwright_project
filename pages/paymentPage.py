import re

from playwright.sync_api import Page

class PaymentPage:
    def __init__(self, page:Page):
        self.page = page
        self.itemQuantity = self.page.locator(".item__quantity")
        #personal information
        self.cardNumberField = self.page.locator('[type="text"]').nth(0)
        self.cvvCodeField= self.page.locator('[type="text"]').nth(1)
        self.nameOnCardField = self.page.locator('[type="text"]').nth(2)

        self.applyCouponField = self.page.locator('[type="text"]').nth(3)
        self.applyCouponButton = self.page.get_by_role("button", name="Apply Coupon")
        self.couponSuccessMessage = self.page.get_by_role('[style*="green"]')

        #shipping information
        self.emailFieldlabel = self.page.locator('[type="text"]').nth(4)
        self.emailField = self.page.locator('[type="text"]').nth(5)
        self.selectCountry = self.page.locator('[placeholder="Select Country"]')

    def getQuantityVaule(self):
        quantityText = self.itemQuantity.text_content()
        match = re.search(r'\d+', quantityText)
        if match:
            number = int(match.group())
            return number
        else:
            print("No value found")

    def enterCardDetails(self, cardnumber:str, cvvCode:str, nameOnCard:str):
        self.cardNumberField.clear()
        self.cardNumberField.fill(cardnumber)
        self.cvvCodeField.fill(cvvCode)
        self.nameOnCardField.fill(nameOnCard)

    def applyCoupon(self, couponCode:str):
        self.applyCouponField.fill(couponCode)
        self.applyCouponButton.click()