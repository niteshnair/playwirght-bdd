from behave import fixture, use_fixture
from playwright.sync_api import (
    Playwright,
    sync_playwright,
    expect,
    Page,
    Browser,
    BrowserContext,
)


@fixture
def playwright_chrome_browser(context):
    context.playwright: Playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    yield context.browser
    context.browser.close()
    context.playwright.stop()


def before_all(context):
    use_fixture(playwright_chrome_browser, context)
