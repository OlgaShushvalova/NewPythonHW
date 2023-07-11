
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте
# модуль fractions.

import fractions

number1: int = int(input("Введите числитель первой дроби "))
number2: int = int(input("Введите знаменатель первой дроби "))
number3: int = int(input("Введите числитель второй дроби "))
number4: int = int(input("Введите знаменатель первой дроби "))

get_sum = (number1 * number4) + (number3 * number2)
get_mult = number1 * number3

get_deno = number2 * number4

result1 = f"Сумма дробей:{get_sum}/{get_deno}"
result2 = f"Произведение дробей:{get_mult}/{get_deno}"

print(result1)
print(result2)

firstFraction = fractions.Fraction(number1, number2)
secondFraction = fractions.Fraction(number3, number4)
result3 = firstFraction + secondFraction
result4 = firstFraction * secondFraction

print(f"Сумма дробей: {result3}")
print(f"Произведение дробей: {result4}")