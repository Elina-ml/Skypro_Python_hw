import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page_allure import FormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(30)
    yield driver
    driver.quit()

@allure.title("Заполнение и отправка формы")
@allure.description("Тест заполняет все поля формы и отправляет ее.")
@allure.feature("Формы")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission(driver):
    page = FormPage(driver)

    with allure.step("Заполнение поля 'first-name'"):
        page.fill_field("first-name", "Иван")

    with allure.step("Заполнение поля 'last-name'"):
        page.fill_field("last-name", "Петров")

    with allure.step("Заполнение поля 'address'"):
        page.fill_field("address", "Ленина, 55-3")

    with allure.step("Заполнение поля 'city'"):
        page.fill_field("city", "Москва")

    with allure.step("Заполнение поля 'country'"):
        page.fill_field("country", "Россия")

    with allure.step("Заполнение поля 'zip-code'"):
        page.fill_field("zip-code", "312321321")

    with allure.step("Заполнение поля 'e-mail'"):
        page.fill_field("e-mail", "test@skypro.com")

    with allure.step("Заполнение поля 'phone'"):
        page.fill_field("phone", "+7985899998787")

    with allure.step("Заполнение поля 'job-position'"):
        page.fill_field("job-position", "QA")

    with allure.step("Заполнение поля 'company'"):
        page.fill_field("company", "SkyPro")

    with allure.step("Отправка формы"):
        page.submit_form()