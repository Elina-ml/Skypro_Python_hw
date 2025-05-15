from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def login_buttons(self, username: str, password: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self) -> None:
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-onesie'))).click()

    def go_to_cart(self) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    def checkout(self) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
        ).click()

    def search_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#first-name'))
        ).send_keys(first_name)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#last-name'))
        ).send_keys(last_name)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#postal-code'))
        ).send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self) -> str:
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        total_value = total_text.replace('Total:', '').replace('$', '').strip()
        return total_value