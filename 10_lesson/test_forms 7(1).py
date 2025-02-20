import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Тестирование заполнение формы ")
@allure.description("Тестирование подсветки полей ")
@allure.feature
@allure.severity("Высокая")
def test_01_form(driver):
    with allure.step("Создаем объект страницы"):
        form_page = FormPage(driver)

    with allure.step("Открытие страницы"):
        form_page.open()

    with allure.step("Заполнение страницы"):
        field_names = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "zip-code", "city", "country",
        "job-position", "company"
    ]

        values = [
        "Иван", "Петров", "Ленина, 55-3", "test@skypro.com",
        "+7985899998787", "", "Москва", "Россия",
        "QA", "SkyPro"
    ]
    with allure.step("Заполнение страницы"):
        form_page.fill_form(field_names, values)

    with allure.step("Нажимаем кнопку Submit"):
        form_page.submit()

    with allure.step("Ожидание появления элемента с ID company"):
        form_page.wait_for_company_element()

    with allure.step("Проверка, что поле Zip code подсвечено красным"):
        assert "danger" in form_page.get_zip_code_class(), "Поле Zip code должно быть подсвечено красным"

    with allure.step("Проверка всех полей на успешное заполнение"):
        fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
        for field_id in fields:
            assert "success" in form_page.get_field_class(field_id), f"Поле {field_id} должно быть подсвечено зеленым"

