"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count: int = 0):
    if num_count == 0:
        raise ValueError("Введите значение больше 1")
    else:
        a, b = 1, 1
        for _ in range(num_count):
            yield a
            a, b = b, a + b


gen = fibonacci(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
