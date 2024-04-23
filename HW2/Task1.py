# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

HEX = 16
hex_digits = "0123456789ABCDEF"
result = ''
negative = False

while True:
    try:
        num = int(input("Введите целое число: "))
        break  
    except ValueError:
        print("Ошибка ввода. Введите целое число.")
  
    
print("Проверка с использованием функции hex():", hex(num))

if num == 0:
    print("Шестнадцатеричное представление числа", num, ":", num)
elif num < 0:
    num = abs(num)
    negative = True
while num > 0:
    index = num % HEX
    result = hex_digits[index] + result
    num //= HEX
print(f'Шестнадцатеричное представление числа: {result}' if negative == False else f'Шестнадцатеричное представление числа: -{result}')
