from playwright.sync_api import Page, expect

from pages.cartPage import CartPage
from pages.loginPage import LoginPage
from pages.orderConfirmationPage import OrderConfirmationPage
from pages.paymentPage import PaymentPage
from pages.productPage import ProductPage


def test_PlaceOrderTest(page:Page):
    productName = "ZARA COAT 3"
    loginpage = LoginPage(page)
    loginpage.navigateToLoginPage("https://rahulshettyacademy.com/client/#/auth/login")
    loginpage.login("jay.aurven@gmail.com", "Manu@5252")
    expect(page).to_have_title("Let's Shop")

    productpage = ProductPage(page)
    productpage.addProductToCart(productName)
    productpage.navigateToCartPage()

    cartpage = CartPage(page)
    expect(cartpage.productNameInCart).to_have_text((productName))
    cartpage.navigateToCheckOut()

    paymentpage = PaymentPage(page)
    totelItemsInCart = paymentpage.getQuantityVaule()
    assert totelItemsInCart==1
    paymentpage.enterCardDetails("4542 9931 9292 2293", "123", "Jay Kumar")
    #paymentpage.applyCoupon("rahulshettyacademy")
    expect(paymentpage.emailFieldlabel).to_have_text("jay.aurven@gmail.com")
    paymentpage.addCountry("India")
    paymentpage.placeOrder()

    confirmationpage = OrderConfirmationPage(page)
    orderid = confirmationpage.getOrderid()
    print(orderid)
