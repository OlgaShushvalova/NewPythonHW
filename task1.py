# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

CHECK_FOUR = 4
CHECK_HUNDRED = 100
CHECK_FOUR_HUNDRED = 400
START_YEAR = 1582
result = ''
year = int(input('Введите год: '))
if year < START_YEAR:
    result = 'Вы ввели неверную дату'
elif year % CHECK_FOUR:
    result = 'Год невисокосный'
elif not year % CHECK_HUNDRED:
    if not year % CHECK_FOUR_HUNDRED:
        result = 'Год високосный'
    else:
        result = 'Год невисокосный'
else:
    result = 'Год високосный'
print(result)