import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage  # Импортируем класс страницы калькулятора


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.title("Тестирование заполнение формы ")
@allure.description("Тестирование подсветки полей ")
@allure.feature
@allure.severity("Высокая")
def test_calculator(driver):
    calculator_page = CalculatorPage(driver)

    with allure.step("Открытие страницы"):
        calculator_page.open()

    with allure.step("Задержка страницы"):
        calculator_page.set_delay("45")

    with allure.step("Выполняем нажатия на кнопки 7 + 8 ="):
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

    with allure.step("Ожидаем результат 15"):
        calculator_page.wait_for_result("15")

    with allure.step("Проверка результата"):
        result = calculator_page.get_result()
    assert int(result) == 15, f"Ожидалось 15, но получено {result}"

