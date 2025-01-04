from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидаем появления текста "Done" или загрузки 4-й картинки
    WebDriverWait(driver, 10).until(
        lambda d: (
            "Done" in d.find_element(By.TAG_NAME, "body").text or
            len(d.find_elements(By.XPATH, "(//img)[4]")) > 0
        )
    )

    # Проверяем наличие текста "Done"
    done_text = driver.find_element(By.TAG_NAME, "body").text
    if "Done" in done_text:
        print("Text 'Done' appeared.")

    # Получаем значение атрибута src у 3-й картинки
    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) >= 3:
        print("Source of the 3rd image:", images[2].get_attribute("src"))

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
