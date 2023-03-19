Feature: Google

    Scenario: Search Google

        Given Url "https://www.google.com/" is open in "Chrome"
        When User enters "Python"
        And Clicks "Google Search"
        And Click on the first search result
        Then Check the title of the page is "Welcome to Python.org"

