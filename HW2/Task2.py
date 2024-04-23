# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
from fractions import Fraction

f1 = str(input('Введите первую дробь вида "a/b": '))
f2 = str(input('Введите вторую дробь вида "a/b": '))

a1, b1 = map(int, f1.split('/'))
a2, b2 = map(int, f2.split('/'))

f1 = Fraction(a1, b1)
f2 = Fraction(a2, b2)
print("Проверка произвдения с использованием функции Fraction():", f1 * f2)
print("Проверка суммы с использованием функции Fraction():", f1 + f2)

b1_temp = b1
b2_temp = b2
while b2_temp:
    b1_temp, b2_temp = b2_temp, b1_temp % b2_temp
    gcd = b1_temp

lcm = (b1*b2)//gcd
print(f'Произведение дробей: {f1}*{f2}={a1*a2}/{lcm}')

a1 *= lcm // b1
a2 *= lcm // b2

print(f'Сумма дробей: {f1}+{f2}={a1 + a2}/{lcm}')



