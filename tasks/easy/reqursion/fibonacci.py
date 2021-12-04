"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci(n, x=0, result=1):
    if n != 1:
        return fibonacci(n - 1, result, x + result)
    else:
        return result


print(fibonacci(6))
