# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_file_path(file_path):
    path = file_path[:file_path.rfind("/")]
    file = file_path[file_path.rfind("/")+1:]
    name, extension = file.split('.')
   
    return path, name, extension

link = "/Users/n.zarubkina/Desktop/GeekBrains/Python/HW1/Task1.py"
print(split_file_path(link))