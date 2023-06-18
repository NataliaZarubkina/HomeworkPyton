def name_data():
    name = input('Введите Ваше имя: ')
    print('Очень красивое имя! (а меня зовут гб_бот, меня создала компания GeekBrains!')
    return name


def surname_data():
    surname = input('Введите Вашу фамилию: ')
    return surname


def phone_data():
    # import re
    phone = input('Введите Ваш телефон: ')
    return phone


def address_data():
    address = input('Введите Ваш адрес: ')
    return address

def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value

