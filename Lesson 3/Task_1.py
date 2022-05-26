"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль."""


def div_func(a, b):
    if b == 0:
        return 'Делить на 0 нельзя'
    return a / b

first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

print(f'{first_number} / {second_number} = {div_func(first_number, second_number)}')