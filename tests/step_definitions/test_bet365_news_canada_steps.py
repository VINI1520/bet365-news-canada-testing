import pytest
from pytest_bdd import scenarios, parsers, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Convert BDD table to a list of dictionaries
def convert_bdd_table(table):
    rows = table.split("\n")
    headers = [header.strip() for header in rows[0].strip().strip("|").split("|")]
    values_table = [dict(zip(headers, [value.strip() for value in row.strip().strip("|").split("|")])) for row in rows[1:]]
    return values_table

# Set up the browser fixture
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Step: Visit the bet365 website
@given('I am on the bet365 website')
def visit_bet365_website(browser):
    browser.get("https://news.on.bet365.ca/en-ca")

# Step: Check the standard categories
@then(parsers.cfparse('I should see the following standard categories:\n{table}'))
def check_standard_categories(browser, table):
    categories = convert_bdd_table(table)

    for category in categories:
        value = category["Category"]
        menu_category = browser.find_element(By.PARTIAL_LINK_TEXT, value)
        assert menu_category.text == value

# Step: Check the headline of the first news article for each category
@then(parsers.cfparse('I should see the headline of the first news article for each category:\n{table}'))
def check_first_news_by_categories(browser, table):
    categories = convert_bdd_table(table)

    for category in categories:
        value = category["Category"]
        menu_category = browser.find_element(By.PARTIAL_LINK_TEXT, value)
        menu_category.click()
        link_title_news = browser.find_element(By.CLASS_NAME, "fsh-TextHeader")
        title_news_first_page = link_title_news.text
        link_title_news.click()
        title_news_second_page = browser.find_element(By.CLASS_NAME, "amc-HeaderText").text.strip()
        assert title_news_first_page == title_news_second_page
