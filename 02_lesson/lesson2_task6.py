def filter_numbers(lst):
    """
    Функция для фильтрации элементов списка, которые меньше 30 и делятся на 3.

    :param lst: Список чисел
    :return: Новый список с отфильтрованными числами
    """
    filtered_numbers = []

    for number in lst:
        if number < 30 and number % 3 == 0:
            filtered_numbers.append(number)

    return filtered_numbers

# Исходный список
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Получение отфильтрованных чисел
result = filter_numbers(lst)

# Вывод результата
print("Элементы, которые меньше 30 и делятся на 3 без остатка:", result)
