# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:

LOWER_LIMIT = 1
UPPER_LIMIT = 200
count = 10

from random import randint
randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
while count > 0:
    print('Попытка ' + str(count))
    count -= 1
    num = int(input('Введи число между ' + str(LOWER_LIMIT) + ' и ' + str(UPPER_LIMIT) + ': '))
    if num < LOWER_LIMIT or num > UPPER_LIMIT:
        print('Неверно')
    elif num == randintnum:
        print('Вы угадали число!')
        break
    elif num > randintnum:
        print('Загаданное число меньше Вашего')
    elif num < randintnum:
        print('Загаданное число больше Вашего')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею. Было загадано число', randintnum)
    quit()
