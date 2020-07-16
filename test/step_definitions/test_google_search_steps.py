import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
GOOGLE_HOME = "https://www.google.com/"

# Scenarios
scenarios('../features/google_search.feature')


# Initialize test functions
@pytest.fixture
def browser():
    chrome_driver = webdriver.Chrome(executable_path='C:/Driver/chromedriver.exe')
    chrome_driver.implicitly_wait(10)
    # Return drivers configuration
    yield chrome_driver
    chrome_driver.quit()


@given('the user goes to Google')
def the_user_goes_to_google(browser):
    browser.get(GOOGLE_HOME)


@when(parsers.parse('he searches for "{text}"'))
def he_searches_for(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.ENTER)


@then(parsers.parse('one of the results should contain "{phrase}"'))
def one_of_the_results_should_contain(browser, phrase):
    xpath = "//h3[@class='LC20lb DKV0Md' and contains(text(), '%s')]" % phrase
    results = browser.find_elements_by_xpath(xpath)
    # Assert
    assert len(results) > 0
