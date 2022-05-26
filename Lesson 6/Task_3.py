# 3. Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def get_income(self):
        return self._income

    def set_income(self, wage, bonus):
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.set_income(wage, bonus)

    def get_full_name(self):
        return ' '.join([self.surname, self.name, self.position])

    def get_total_income(self):
        return self.get_income()['wage'] + self.get_income()['bonus']


person = Position('Максим', 'Богачев', 'IT manager', 20000, 5000)

person2 = Position('Алексей', 'Чижов', 'IT spec', 10000, 2000)

print(person.get_full_name())
print(person.get_total_income())

print(person2.get_full_name())
print(person2.get_total_income())
