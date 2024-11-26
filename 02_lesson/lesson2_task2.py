def is_year_leap(year):
    """
    Проверяет, является ли год высокосным.

    :param year: Год (число)
    :return: True, если год высокосный, иначе False
    """
    return year % 4 == 0

# Выбор года для проверки
year_to_check = 2024  # Вы можете изменить этот год на любой другой

# Вызов функции и сохранение результата
is_leap_year = is_year_leap(year_to_check)

# Вывод результата на консоль
print(f"Год {year_to_check}: {is_leap_year}")
