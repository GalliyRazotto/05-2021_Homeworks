"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [x**2 for x in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):

    dividers = []
    for i in range(1, number + 1):
        if number % i == 0:
            dividers.append(i)
    if len(dividers) == 2:
        return True
    else:
        return False


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if 'odd' in filter_type:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif 'even' in filter_type:
        return list(filter(lambda x: x % 2 == 1, numbers))
    elif 'prime' in filter_type:
        return list(filter(is_prime, numbers))
