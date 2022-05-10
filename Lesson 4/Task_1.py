# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv


def salary_calc(pon=0, ch=0, bonus=0):
    return (float(pon) * float(ch)) + float(bonus)


script_name, productivity_on_hour, cost_hour, bonus = argv

print(f'Зарплата сотрудника составляет: {salary_calc(productivity_on_hour, cost_hour, bonus)} руб.')
