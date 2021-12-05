def fibonacci():
    fib1 = 0
    fib2 = 1
    i = 1
    while True:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        yield fib1


fibonacci_gen = fibonacci()

print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
