# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов

my_list = [1, 1, 2, 3, 5, 6, 6, 9]

result = []
for num in my_list:
    if my_list.count(num) > 1:
        result.append(num)

print(set(result))