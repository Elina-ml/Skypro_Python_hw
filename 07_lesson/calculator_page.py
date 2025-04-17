from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def locator_for(self, query):
        delay = self.driver.find_element(
            By.CSS_SELECTOR, "input[id='delay']")
        delay.clear()
        delay.send_keys(query)

    def det_buttons(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def check_results(self):
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))
        return self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
