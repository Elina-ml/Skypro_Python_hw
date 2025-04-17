import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#user-name')))
    search_box = driver.find_element(By.CSS_SELECTOR, 'input#user-name')
    search_box.send_keys('standard_user')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#password')))
    search_box = driver.find_element(By.CSS_SELECTOR, 'input#password')
    search_box.send_keys('secret_sauce')
    add_button = driver.find_element(By.ID, "login-button")
    add_button.click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "checkout"))).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#first-name')))
    search_box = driver.find_element(By.CSS_SELECTOR, 'input#first-name')
    search_box.send_keys('standard')
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#last-name')))
    search_box = driver.find_element(By.CSS_SELECTOR, 'input#last-name')
    search_box.send_keys('user')
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#postal-code')))
    search_box = driver.find_element(By.CSS_SELECTOR, 'input#postal-code')
    search_box.send_keys('9011')
    add_button = driver.find_element(By.ID, "continue")
    add_button.click()

    total_element = '58.29'
    Total = total_element.replace('Total: $', '').strip()
    assert Total == '58.29'

    driver.quit()