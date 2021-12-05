"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    fac = 1
    i = 1
    while True:
        fac *= i
        i += 1
        yield fac


factorial_gen = factorial()
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
