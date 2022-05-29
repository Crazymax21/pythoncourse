# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint
from math import fsum

digit_list = [str(randint(1, 100)) for el in range(10)]

with open('task_5.txt', 'w', encoding='utf-8') as task5_file:
    print(' '.join(digit_list), file=task5_file)

with open('task_5.txt', 'r', encoding='utf-8') as task5_file:
    digit_list = [int(el) for el in task5_file.read().split(' ')]
    print(f'Сумма чисел: {digit_list} = {sum(digit_list)}')
