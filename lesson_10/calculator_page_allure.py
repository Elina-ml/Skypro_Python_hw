from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalcMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
                        "slow-calculator.html")

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button: str) -> None:
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    def click_buttons(self, buttons: list) -> None:
        for button in buttons:
            self.click_button(button)

    def wait_for_result(self, expected_result: str, delay: int) -> None:
        # Р”РѕР±Р°РІР»СЏРµРј +1 СЃРµРєСѓРЅРґСѓ Рє Р·Р°РґРµСЂР¶РєРµ РґР»СЏ РЅР°РґРµР¶РЅРѕСЃС‚Рё
        WebDriverWait(self.driver, delay + 1).until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), expected_result)
        )

    def get_result(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "screen").text

