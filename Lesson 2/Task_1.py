# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

user_list = [1, 'my data', 45.6, ['first', 10], ('tuple', 20), {'1': 'dict'}]

for item in user_list:
    print(type(item))


