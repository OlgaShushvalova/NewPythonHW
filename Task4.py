# Создайте функцию генератор чисел Фибоначчи

def num_fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for i in num_fib(10):
    print(i)