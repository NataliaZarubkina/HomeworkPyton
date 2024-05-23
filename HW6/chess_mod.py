#Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
#Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

__all__ = ['validate_queens']

def validate_queens(positions):
    for i in range(8):
        for j in range(i+1, 8):
            # проверка на наличие на одной строке или диагонали
            if positions[i] == positions[j] or \
                positions[i] - i == positions[j] - j or \
                positions[i] + i == positions[j] + j:
                return False
    return True