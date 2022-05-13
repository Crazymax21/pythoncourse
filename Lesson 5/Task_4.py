# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

digits = {
    '1':'Один',
    '2':'Два',
    '3':'Три',
    '4':'Четыре'
}

with open('task_4.txt', 'r', encoding='utf-8') as task4_file:
    with open('task_4_rus.txt', 'w', encoding='utf-8') as task4rus_file:
        for file_string in task4_file.read().split('\n'):
            print(f'{digits[file_string.split(" — ")[1]]} - {file_string.split(" — ")[1]}')
            print(f'{digits[file_string.split(" — ")[1]]} - {file_string.split(" — ")[1]}', file=task4rus_file)
