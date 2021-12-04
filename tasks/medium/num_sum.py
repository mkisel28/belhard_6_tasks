"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n, sum=0):
    if len(str(n)) == 0:
        return sum
    else:
        return sum_of_numbers(str(n)[1:], sum + int(str(n)[0]))


print(sum_of_numbers(666))
