# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

things_friends = {
    "Петя": ("вода", "нож", "печенье"),
    "Катя": ("зонт", "вода", "телефон"),
    "Вася": ("кола", "дрова", "веревка")
}
def list_things_friends(dict_list):
    list_things = []
    for things in dict_list.values():
        list_things += things
    return list_things

def unique_things (dict_list):
    name_not_things = []
    new_things = {}
    count = 0
    for key, value in things_friends.items():
        name_not_things.append(key)
        new_things[key] = []
        for j in value:
            for k in list_things_friends(things_friends):
                if k == j:
                    count += 1
            if count == 1:
                new_things[key] += [j]
            if count > 1:
                name_not_things.remove(key)
            count = 0
    print("Имя друга, у которого отсутствует вещь, которая дублируется у остальных", name_not_things)
    return new_things

print(f"Вещи которые взяли все три друга{list_things_friends(things_friends)}")
print(f"Уникальные вещи {unique_things(things_friends)}")