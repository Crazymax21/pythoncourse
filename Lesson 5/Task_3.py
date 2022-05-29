# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

average_sum = 0
staff_count = 0

with open('task_3.txt', 'r', encoding='utf-8') as task3_file:
    print(f'Сотрудники с зарплатой менее 20000:')
    for person_data in task3_file.read().split('\n'):
        person_data_list = person_data.split(' ')
        if int(person_data_list[1]) < 20000:
            print(f'{person_data_list}')
        staff_count += 1
        average_sum += int(person_data_list[1])
    print('Средняя зарплата сотрудников: ', average_sum/staff_count)



