# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

string_count = 0
words_count = 0

with open('task_2.txt', 'r', encoding="utf-8") as task2_file:
    for file_string in task2_file:
        string_count += 1
        words_count = len(file_string.split(' '))
        print(f'В строке №{string_count} - {words_count} слов')

