from playwright.sync_api import sync_playwright
from objects import login_page

def test_login_1():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto(login_page.url)
    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.get_by_text('Login').click()
    browser.close()