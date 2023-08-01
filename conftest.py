import pytest
from selenium import webdriver


@pytest.fixture()
def setup(self):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.credence.in/login")
    return driver