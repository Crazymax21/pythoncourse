# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.


from itertools import count

with open('lesson1.txt', 'w') as lesson1_file:
    for i in count(0):
        user_string = input(f'Введите строку №{i + 1}: ')
        if str == '':
            break
        print(user_string, file=lesson1_file)
