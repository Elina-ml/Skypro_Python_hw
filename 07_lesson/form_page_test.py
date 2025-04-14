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
    page.search_for("Иван")
    page.search_for("Петров")
    page.search_for("Ленина, 55-3")
    page.search_for("")
    page.search_for("Москва")
    page.search_for("Россия")
    page.search_for("test@skypro.com")
    page.search_for("+7985899998787")
    page.search_for("QA")
    page.search_for("SkyPro")
