from playwright.sync_api import (
    Playwright,
    sync_playwright,
    expect,
    Page,
    Browser,
    BrowserContext,
)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("Python")
    page.get_by_role("button", name="Google Search").first.click()
    page.get_by_role(
        "link", name="Welcome to Python.org Python https://www.python.org"
    ).click()

    # ---------------------
    context.close()
    browser.close()


class SearchPage:
    def __init__(self, browser: Browser, url) -> None:
        self.browser: Browser = browser
        self.context: BrowserContext = self.browser.new_context()
        self.page: Page = self.context.new_page()
        self.url = url

    def open_url(self):
        self.page.goto(self.url)

    def enter_search_text(self, text: str):
        self.page.get_by_role("combobox", name="Search").fill(text)

    def click_search_button(self, button_name):
        self.page.get_by_role("button", name=button_name).first.click()

    def click_first_result_link(self):
        self.page.get_by_role(
            "link", name="Welcome to Python.org Python https://www.python.org"
        ).click()

    def check_title_result_page(self, title_text):
        title_actual = self.page.title()
        assert (
            title_actual == title_text
        ), f"Title {title_actual} does not match expected {title_text}"

    def __del___(self):
        if self.context:
            self.context.close()
