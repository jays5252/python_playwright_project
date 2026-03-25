from playwright.sync_api import Page, expect

def test_LaunchBrowser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

def test_navigateUrlUsingPage(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title(("Google"))