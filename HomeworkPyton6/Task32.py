a = int(input('Введите минимум:'))
d = int(input('Введите максимум:'))
n = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
if a>d:
    print ('Неверный ввод!')
else:
    for i in range(len(n)):
        if a<n[i]<d:
            print(i, end=' ')
