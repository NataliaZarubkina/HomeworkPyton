from data_create import name_data, surname_data, phone_data, address_data, search_parameters


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас данные из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('Вывожу данные для Вас данные из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записей
        print(f'Какое поле вы хотите изменить?\n{data_first[number_journal]}')
        data_temp=data_first[number_journal].split()
        field = int(input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n4 - Адрес\n'))
        if field == 1:
            data_temp[0] = input('Введите фамилию: ')
        elif field == 2:
            data_temp[1] = input('Введите имя: ')
        elif field == 3:
            data_temp[2] = input('Введите номер телефона: ')
        elif field == 4:
            data_temp[3] = input('Введите адрес: ')
        data_first = data_first[:number_journal] + [f'{data_temp[0]}\n{data_temp[1]}\n{data_temp[2]}\n{data_temp[3]}\n'] + \
                     data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Какое поле вы хотите изменить?\n{data_first[number_journal]}')
        data_temp=data_first[number_journal].split()
        field = int(input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n4 - Адрес\n'))
        if field == 1:
            data_temp[0] = input('Введите фамилию: ')
        elif field == 2:
            data_temp[1] = input('Введите имя: ')
        elif field == 3:
            data_temp[2] = input('Введите номер телефона: ')
        elif field == 4:
            data_temp[3] = input('Введите адрес: ')
        data_first = data_first[:number_journal] + [f'{data_temp[0]}\n{data_temp[1]}\n{data_temp[2]}\n{data_temp[3]}\n'] + \
                     data_first[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        search_field, search_value = search_parameters()
        search_result = []
        for contact in data_first:
            if contact[int(search_field) - 1] == search_value:
                search_result.append(contact)
        if len(search_result) == 1:
            return search_result[0]
        elif len(search_result) > 1:
            print('Найдено несколько контактов')
            for i in range(len(search_result)):
                print(f'{i + 1} - {search_result[i]}')
            num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
            return search_result[num_count - 1]
        else:
            print('Контакт не найден')
        print()
        data_first.remove(number_to_change)
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    
    else:
        search_field, search_value = search_parameters()
        search_result = []
        for contact in data_second:
            if contact[int(search_field) - 1] == search_value:
                search_result.append(contact)
        if len(search_result) == 1:
            return search_result[0]
        elif len(search_result) > 1:
            print('Найдено несколько контактов')
            for i in range(len(search_result)):
                print(f'{i + 1} - {search_result[i]}')
            num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
            return search_result[num_count - 1]
        else:
            print('Контакт не найден')
        print()
        data_second.remove(number_to_change)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!') 
