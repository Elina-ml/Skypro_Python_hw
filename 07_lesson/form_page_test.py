import pytest
from pyzstd import finalize_dict
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from form_page import FormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(30)
    yield driver
    driver.quit()

def test_form(driver):
    page = FormPage(driver)
    page.fill_field("first-name", "Иван")
    page.fill_field("last-name", "Петров")
    page.fill_field("address", "Ленина, 55-3")
    page.fill_field("city", "Москва")
    page.fill_field("country", "Россия")
    page.fill_field("zip-code", "312321321")
    page.fill_field("e-mail", "test@skypro.com")
    page.fill_field("phone", "+7985899998787")
    page.fill_field("job-position", "QA")
    page.fill_field("company", "SkyPro")
