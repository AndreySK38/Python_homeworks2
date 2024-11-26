def create_list_using_range():
    """
    Функция для создания списка [18, 14, 10, 6, 2] с помощью функции range().

    :return: Список чисел
    """
    # Используем range() для создания списка
    # range(start, stop, step) - start = 18, stop = 0 (не включительно), step = -4
    lst = list(range(18, 0, -4))
    return lst


# Создание списка
result_list = create_list_using_range()

# Вывод результата
print("Список, созданный с помощью функции range():", result_list)
