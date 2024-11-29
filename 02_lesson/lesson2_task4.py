
def fizz_buzz(n):
    """
    Печатает числа от 1 до n, заменяя числа, делящиеся на 3, 5 и 15
    на соответствующие строки: Fizz, Buzz и FizzBuzz.

    :param n: Конечное число (число)
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Пример использования функции
if __name__ == "__main__":
    n = 17  # Вы можете изменить это значение на любое другое
    fizz_buzz(n)
