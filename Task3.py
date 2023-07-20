# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой
# длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем
# словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка
# умноженная на процент премии

names = ['Петр', 'Катя', 'Иван', 'Елена']
salary = [15000, 20000, 30000, 50000]
premium = ['10.25%', '12.00%', '9.50%', '12.50%']


def size_premium(names: list[str], salary: list[int], premium: list[str]) -> dict[str: float]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (float(i[:-1]) for i in premium))}.items()


print(*(size_premium(names, salary, premium)))
