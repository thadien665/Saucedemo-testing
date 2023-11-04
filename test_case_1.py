from playwright.sync_api import sync_playwright, expect
from objects import login_page

def test_t01():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(login_page.url)
    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.get_by_text('Login').click()
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    browser.close()

def test_t02():
    playwright = sync_playwright().start()
    browser =  playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(login_page.url)
    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret')
    page.get_by_text('Login').click()
    expect(page.get_by_text('Epic sadface: username and password do not match any user in this service')).to_be_visible()
    browser.close()