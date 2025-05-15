import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_page_allure import ShopPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@allure.title("Проверка оформления заказа")
@allure.description("Тест авторизации и оформления заказа на сайте saucedemo.com")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_order_process(driver):
    page = ShopPage(driver)
    with allure.step("Авторизация пользователя"):
       page.login_buttons("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
       page.add_to_cart()

    with allure.step("Переход в корзину"):
       page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
       page.checkout()

    with allure.step("Заполнение формы данных покупателя"):
       page.search_form("standard", "user", "9011")

    with allure.step("Проверка итоговой суммы заказа"):
       total_price = page.get_total_price()
       assert total_price == "58.29", f"Ожидалась сумма 58.29, получена {total_price}"