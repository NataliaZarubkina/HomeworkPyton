#Найдите сумму цифр трехзначного числа
i = int(input("Введите трехзначное число: "))
summa = 0
while i > 0:
    x = i % 10
    summa = summa + x
    i = i // 10
print("Сумма чисел = ", summa) 