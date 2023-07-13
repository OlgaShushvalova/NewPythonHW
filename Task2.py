
#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

list_element = [1, 5, 5, 1, 4, 3, 4, 7]

def double_list(list_element):
    res = set()
    for el in list_element:
        counter = list_element.count(el)
        if counter > 1:
            res.add(el)
    return list(res)

print(f"Список дублирующихся элементов {double_list(list_element)}")