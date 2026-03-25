from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page:Page):
        self.page = page
        self.allProduct = self.page.locator(".card-body")
        self.cartPageLinkButton = self.page.locator('[routerlink="/dashboard/cart"]')

    def addProductToCart(self, productName:str):
        productToBeAddedtoCart = self.allProduct.filter(has_text=productName)
        productToBeAddedtoCart.get_by_role("button", name= "Add To Cart").click()

    def navigateToCartPage(self):
        self.cartPageLinkButton.click()