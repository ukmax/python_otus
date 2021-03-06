"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 400, 25, 49]
    """
    new_list = []
    for n in numbers:
        new_list.append(n * n)
    return new_list


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return n == i


def filter_numbers(numbers, filter_types):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """
    res = []
    if filter_types == ODD:
        res = filter(lambda x: x % 2 == 1, numbers)
    if filter_types == EVEN:
        res = filter(lambda x: x % 2 == 0, numbers)
    if filter_types == PRIME:
        res = filter(is_prime, numbers)

    return list(res)
