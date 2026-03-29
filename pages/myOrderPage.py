from operator import truediv

from playwright.sync_api import Page

class MuOrderPage:
    def __init__(self, page:Page):
        self.page = page
        self.orderList = self.page.locator('tr.ng-star-inserted')

    def verifyOrderInHistoryTable(self, orderId:str):
       allOrders = self.orderList.locator('th')
       if allOrders.filter(has_text=orderId).is_visible():
           return "true"
       else:
           return "false"

    def navigateToOrderDetails(self, orderid:str):
       OrderRow =  self.orderList.filter(has_text=orderid)
       OrderRow.get_by_role("button", name="View").click()