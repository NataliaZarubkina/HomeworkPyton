#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = int(input('Введите первое число:'))
B = int(input('Введите второе число:'))
def exp(A, B):
    if B == 0:
        return 1
    return A*exp(A, B-1)
print(exp(A, B))