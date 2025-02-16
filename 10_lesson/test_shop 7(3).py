import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_page import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.title("Тестирование заполнение формы ")
@allure.description("Тестирование подсветки полей ")
@allure.feature
@allure.severity("Высокая")
def test_purchase_total(driver):
    shop_page = ShopPage(driver)

    with allure.step("Открываем сайт магазина"):
        shop_page.open()

    with allure.step("Авторизуемся как пользователь standard_user"):
        shop_page.login('standard_user', 'secret_sauce')

    with allure.step("Добавляем товары в корзину"):
        items_to_add = [
        'sauce-labs-backpack',
        'sauce-labs-bolt-t-shirt',
        'sauce-labs-onesie'
    ]
    shop_page.add_to_cart(items_to_add)

    with allure.step("Переходим в корзину и выполняем Checkout"):
        shop_page.go_to_cart()
    shop_page.checkout('Евгений', 'Геранин', '454000')

    with allure.step("Получаем итоговую стоимость"):
        total = shop_page.get_total()
    print(total)

    # Проверка итоговой стоимости
    assert total == 'Total: $58.29', f"Ожидалось 'Total: $58.29', но получено '{total}'"

    print("Тест пройден успешно!")