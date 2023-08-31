# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

import doctest


def triangle(a: int, b: int, c: int):
    if 1_000_000_000 < a or a <= 0 or \
       1_000_000_000 < b or b <= 0 or \
       1_000_000_000 < c or c <= 0:
        return f'Вы ввели недопустимые значения попробуйте снова!'

    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        return f'стороны треугольника должны быть типа int..'

    if a < b + c and b < a + c and c < a + b:
        if a == b and a == c:
            return f'Треугольник  является равносторонним!'
        elif a == b or a == c or a == c:
            return f'Треугольник является равнобедренним!'
        else:
            return f'Треугольник является разносторонним!'
    else:
        return f'Такого треугольника не существует!'


doctest.testfile('doctest_triangle.md', verbose=True)





