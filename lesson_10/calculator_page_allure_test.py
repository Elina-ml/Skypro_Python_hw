import pytest
import allure
from selenium import webdriver
from calculator_page_allure import CalcMainPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 15),
        ("9", "-", "3", "6", 10),
        ("4", "x", "5", "20", 20),
        ("8", "Г·", "2", "4", 5),
    ],
)
@allure.title("Калькулятор - проверка арифметических операций")
@allure.description("Тест проверяет корректность выполнения арифметических операций на странице калькулятора.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_flow(driver, num1, operation, num2, expected_result, delay):
    main_page = CalcMainPage(driver)
    with allure.step("Открытие страницы калькулятора"):
        main_page.open()
    with allure.step(f"Установка задержки {delay} секунд"):
       main_page.set_delay(delay)
    with allure.step(f"Ввод чисел и операции {num1} {operation} {num2}"):
       main_page.click_buttons([num1, operation, num2, "="])
    with allure.step(f"Ожидание результата '{expected_result}'"):
       main_page.wait_for_result(expected_result, delay)
    with allure.step("Проверка результата вычислений"):
       result = main_page.get_result()
       assert result == expected_result, f"Expected result:{expected_result}, but got:{result}"
