# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

N = int(input('Введите количество элементов массива:'))
data = [int(i) for i in input("Введите массив: ").split()]
if N != len(data):
    print("Введено неверное количество элементов")
else:
    X = int(input('Введите число: '))
    num=0
    for i in range(len(data)):
        if (X-data[i]) < X - num and X-data[i]>0:
            num = i
print(data[num])

