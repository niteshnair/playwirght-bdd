from behave import given, when, then, step
from ui.search_page import SearchPage


@given('Url "{url}" is open in "{browser}"')
def open_url(context, url, browser):
    if browser.casefold() == "Chrome".casefold():
        context.search_page: SearchPage = SearchPage(context.browser, url)
        context.search_page.open_url()


@when('User enters "{search_string}"')
def enter_text(context, search_string):
    sp: SearchPage = context.search_page
    sp.enter_search_text(search_string)


@step('Clicks "{button_name}"')
def click_button(context, button_name):
    sp: SearchPage = context.search_page
    sp.click_search_button(button_name)


@step("Click on the first search result")
def click_first_result(context):
    sp: SearchPage = context.search_page
    sp.click_first_result_link()


@then('Check the title of the page is "{title_text}"')
def check_results_displayed(context, title_text):
    sp: SearchPage = context.search_page
    sp.check_title_result_page(title_text)
