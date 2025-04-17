import self
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_field(self, first_name, last_name, zip_code):
        self.driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self.driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self.driver.find_element(By.NAME, "zip-code").send_keys(zip_code)

    def submit_form(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(By.XPATH, "//button[text()='Submit']")).click()