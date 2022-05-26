"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов."""


def max_sum(a, b, c):
    list_args = sorted([a, b, c], reverse=True)
    return list_args[0], list_args[1], sum(list_args[:2])


max_1, max_2, sum_max = max_sum(10, 3, 20)

print(f'{max_1} + {max_2} = {sum_max}')
