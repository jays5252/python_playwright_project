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

        self.placeOrderButton = self.page.locator(".action__submit")

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
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(3000)


    def addCountry(self, countryNam:str):
        self.selectCountry.press_sequentially(countryNam, timeout=2000)
        countryList = self.page.locator('.ta-results button')
        for i in range(countryList.count()):
            countryName = countryList.nth(i).text_content()
            country = countryName.lstrip()
            if country==countryNam:
                countryList.nth(i).click()
                break

    def placeOrder(self):
        self.placeOrderButton.click()