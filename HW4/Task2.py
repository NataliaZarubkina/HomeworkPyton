# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление.


def create_argument_dict(**kwargs):
    argument_dict = {}
    
    for key, value in kwargs.items():
        if not hash(key):
            key = str(key)
        argument_dict[value] = key
    
    return argument_dict

result = create_argument_dict(name="John", age=25, city="New York", salary=5000)

for key, value in result.items():
    print(f"{key}: {value}")