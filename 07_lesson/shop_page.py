from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def login_buttons(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys('standard_user')
        self.driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'))).click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-onesie'))).click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
            checkout_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']")))
            checkout_button.click()

    def search_form(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#first-name')))
        self.driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys(first_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#last-name')))
        self.driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys(last_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "postal-code")))
        self.driver.find_element(By.NAME, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
