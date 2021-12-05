"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number(n):
    for i in range(n):
        if i % 2 == 0 and i != 0:
            yield i


even_gen = get_even_number(10)
print(next(even_gen))
print(next(even_gen))
print(next(even_gen))
print(next(even_gen))
