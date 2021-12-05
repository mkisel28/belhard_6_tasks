"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n: int):
    return sum_of_numbers(n / 10) + n % 10 if n > 9 else n


print(sum_of_numbers(666))
