# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

backpack_capacity = int(input("Введите грузоподъемность рюкзака: "))
items = {
    'Спальник': 2,
    'Палатка': 4,
    'Еда': 3,
    'Вода': 5,
    'Фонарик': 1
}

backpack = []
total_weight = 0 

for item, weight in items.items():
        if total_weight + weight <= backpack_capacity:
            backpack.append(item)
            total_weight += weight

print("Вещи, которые помещаются в рюкзак:")
for item in backpack:
    print(item)