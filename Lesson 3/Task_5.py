"""5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу."""


def sum_numbers(ssum=0):
    user_string = input('Введите числа через пробел: ')
    user_list = user_string.split(' ')
    for num in user_list:
        if num != '=':
            ssum += int(num)
        else:
            break
    if num == '=':
        print(f'Итоговая сумма: {ssum}')
        return print(f'Завершено')
    else:
        print(f'Текущий результат: {ssum}')
        sum_numbers(ssum)


sum_numbers()
