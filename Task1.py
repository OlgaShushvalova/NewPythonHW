# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.

HEX_SYSTEM = 16

number: int = int(input('\nВведите целое число: '))
def convert_num(number: int, HEX_SYSTEM) -> str:
    result: str = ''
    while number != 0:
        mod: str = str(number % HEX_SYSTEM)
        result = mod + result
        number //= HEX_SYSTEM
    return result

convert: str = convert_num(number, HEX_SYSTEM)
print(f'\nРезультат: {convert}')
print(f'\nЧисло в шестнадцатеричной системе счисления: {hex(number)[2:]}')
