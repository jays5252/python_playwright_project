from playwright.sync_api import Page, expect

from pages.cartPage import CartPage
from pages.loginPage import LoginPage
from pages.myOrderPage import MuOrderPage
from pages.orderConfirmationPage import OrderConfirmationPage
from pages.orderSummaryPage import OrderSummaryPage
from pages.paymentPage import PaymentPage
from pages.productPage import ProductPage


def test_PlaceOrderTest(page:Page):

    #testData
    productName = "ZARA COAT 3"
    user_email = "jay.aurven@gmail.com"
    password = "Manu@5252"
    country_name = "India"


    loginpage = LoginPage(page)
    loginpage.navigateToLoginPage("https://rahulshettyacademy.com/client/#/auth/login")
    loginpage.login(user_email, password)
    expect(page).to_have_title("Let's Shop")

    productpage = ProductPage(page)
    productpage.addProductToCart(productName)
    productpage.navigateToCartPage()

    cartpage = CartPage(page)
    expect(cartpage.productNameInCart).to_have_text((productName))
    cartpage.navigateToCheckOut()

    paymentpage = PaymentPage(page)
    totalItemsInCart = paymentpage.getQuantityVaule()
    assert totalItemsInCart == 1
    paymentpage.enterCardDetails("4542 9931 9292 2293", "123", "Jay Kumar")
    paymentpage.applyCoupon("rahulshettyacademy")
    expect(paymentpage.emailFieldlabel).to_have_text(user_email)
    paymentpage.addCountry(country_name)
    paymentpage.placeOrder()

    confirmation = OrderConfirmationPage(page)
    orderid = confirmation.getOrderid()
    print(orderid+" :order Id")
    confirmation.navigateToOrderHistory()

    orderPage = MuOrderPage(page)
    #assert (orderPage.verifyOrderInHistoryTable(orderid)) == "true"
    orderPage.navigateToOrderDetails(orderid)

    orderSummaryPage = OrderSummaryPage(page)
    userCountry = orderSummaryPage.getCountryFromOrder().rstrip()
    userEmail = orderSummaryPage.getEmailFromOrder()
    productName = orderSummaryPage.getProductName()
    productOrderId = orderSummaryPage.getOrderIdFromOrder()

    assert userCountry==country_name
    assert userEmail == user_email
    assert productName == productName
    assert productOrderId == orderid

