def month_to_season(month):
    """
    Возвращает название сезона по номеру месяца.

    :param month: Номер месяца (1-12)
    :return: Название сезона
    """

    if month < 1 or month > 12:
        return "Некорректный номер месяца. Пожалуйста, введите число от 1 до 12."

    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    else:  # month in [9, 10, 11]
        return "Осень"


# Пример использования функции
if __name__ == "__main__":
    month = 2  # Вы можете изменить это значение на любое другое
    season = month_to_season(month)
    print(f"Месяц {month} - это {season}.")
