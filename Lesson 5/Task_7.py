# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

firm_list = []
firm_dict = {}
firm_profit_list = []

with open('task_7.txt', 'r', encoding='utf-8') as task7_file:
    strings_list = task7_file.read().split('\n')
    for string in strings_list:
        firm_data = string.split(' ')
        firm_profit = int(firm_data[2]) - int(firm_data[3])
        firm_dict[firm_data[0]] = firm_profit
        if firm_profit > 0:
            firm_profit_list.append(firm_profit)

firm_list.append(firm_dict)
firm_list.append({'average_profit': round(sum(firm_profit_list) / len(firm_profit_list), 2)})

print(firm_list)

with open('task_7.json', 'w', encoding='utf-8') as task7_json_file:
    json.dump(firm_list, task7_json_file)
