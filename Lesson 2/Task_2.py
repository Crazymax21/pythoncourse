# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input().

user_str = input('Введите список через пробел: ')
user_list = user_str.split(' ')

for i in range(1, len(user_list) if len(user_list) % 2 == 0 else len(user_list) - 1, 2):
    tmp = user_list[i - 1]
    user_list[i - 1] = user_list[i]
    user_list[i] = tmp

print(user_list)
