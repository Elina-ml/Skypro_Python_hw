import pytest
from pyzstd import finalize_dict
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shop_page import ShopPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_auto(driver):
    page = ShopPage(driver)
    page.login_buttons("standard_user", "secret_sauce")
    page.add_to_cart()
    page.go_to_cart()
    page.checkout()
    page.search_form("standard", "user", "9011")

def total():
    total_element = '58.29'
    Total = total_element.replace('Total: $', '').strip()
    assert Total == '58.29'
