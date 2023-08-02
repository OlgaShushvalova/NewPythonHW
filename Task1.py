# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def counter(n: int):
    list_counter = []

    def deco(func: callable):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                list_counter.append(func(*args, **kwargs))
            return list_counter
        return wrapper
    return deco


@counter(5)
def test(*args) -> int:
    return sum(args)


print(test(25, 35, 45))