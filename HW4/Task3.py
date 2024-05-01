"""
    Напишите программу банкомат.
    Начальная сумма равна нулю
    Допустимые действия: пополнить, снять, выйти
    Сумма пополнения и снятия кратны 50 у.е.
    Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
    После каждой третей операции пополнения или снятия начисляются проценты - 3%
    Нельзя снять больше, чем на счёте
    При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
    Любое действие выводит сумму денег
"""
import decimal
from decimal import Decimal


MIN_SUM = Decimal(50)
PERCENT_COMISSION = Decimal(0.015)
MIN_COMISSION = Decimal(30)
MAX_COMISSION = Decimal(600)
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = Decimal(5_000_000)
TAX_RATE = Decimal(0.1)

give_get = []

def menu(balance: Decimal, count: int, is_flag: bool):
    dct = {'1': 'пополнить счет',
           '2': 'снять со счета',
           '3': 'выйти из программы'}
    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_RATE)
    choice = input('Введите команду: ')
    if choice == '3':
        print('Баланс равен: ', balance)
        is_flag = False
        return balance, is_flag
    elif choice == '1':
        balance = give_money(balance)
        count += 1
    elif choice == '2':
        balance = get_money(balance)
        count += 1
    else:
        print('Неверная команда!')
    if count % 3 == 0:
        balance *= (1 + BONUS)
    print('Баланс равен: ', balance, "Операции: ", give_get)
    return balance, is_flag

def get_money(balance: Decimal):
    money_to_get = Decimal(input('Введите сумму снятия: '))
    percent = money_to_get * PERCENT_COMISSION

    if money_to_get % MIN_SUM == 0:
        if percent <= MIN_COMISSION:
            percent = MIN_COMISSION
        elif percent > MAX_COMISSION:
            percent = MAX_COMISSION

        if (money_to_get + percent) <= balance:
            give_get.append('-' + str(money_to_get))
            return balance - (money_to_get + percent)
        else:
            print('Недостаточно средств')
            return balance
    else:
        print('Ошибка снятия денег - сумма должна быть кратна 50')
        return balance

def give_money(balance: Decimal):
    money_to_give = Decimal(input('Введите сумму пополнения: '))
    if money_to_give % MIN_SUM == 0:
        give_get.append('+' + str(money_to_give))
        return balance + money_to_give
    else:
        print('Ошибка пополнения - сумма не кратная 50 у.е.')
        return balance


if __name__ == '__main__':
    print('Добро пожаловать в программу БАНКОМАТ')
    balance = 0
    count = 1
    is_flag = True
    while is_flag:
        balance, is_flag = menu(balance, count, is_flag)
