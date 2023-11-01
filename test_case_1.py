from playwright.sync_api import sync_playwright
from objects import login_page

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless = False)
context = browser.new_context()
page = context.new_page()
page.goto(login_page.url)
print(login_page.url.title())
