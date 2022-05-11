# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

rating_list = sorted([5, 3, 6, 1, 2, 9, 3], reverse=True)

input_item = ''

while input_item != '0':
    input_item = int(input('Введите элемент(0 - закончить ввод): '))
    if input_item == 0:
        break
    if input_item in rating_list:
        new_element_position = rating_list.index(input_item) + rating_list.count(input_item)
        rating_list.insert(new_element_position, input_item)
    else:
        rating_list.append(input_item)
        new_element_position = rating_list.index(input_item)

    print(f'На позицию {new_element_position}, добавлен элемент {input_item}')
    rating_list = sorted(rating_list, reverse=True)
    print(rating_list)
