from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_field(self, field_name: str, value: str) -> None:
        self.driver.find_element(By.NAME, field_name).send_keys(value)

    def submit_form(self) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        ).click()