# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class IsExist(Exception):

    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt

class Store:
    def __init__(self):
        self.equipments = {}

    def add_equipment(self, place, equipment):
        if place in self.equipments.keys() and self.equipments[place] == equipment:
            print('Оборудование уже находится на этом месте')
            return False
        elif self.get_values(self.equipments, equipment):
            print(f'Это оборудование уже лежит на складе. Место {self.get_values(self.equipments, equipment)}')
            return False
        elif place in self.equipments.keys() and self.equipments[place] != equipment:
            print(f'На месте {place} лежит {self.equipments[place]}')
            return False
        else:
            self.equipments[place] = equipment
            print('Оборудование добавлено на склад')
            return True

    def __str__(self):
        for i, el in self.equipments.items():
            print(f'{i}: {el}')
        return ''

    def remove_equipment(self, equipment):
        if self.get_values(self.equipments, equipment):
            self.equipments.pop(self.get_values(self.equipments, equipment))
            print(f'Оборудование {equipment} убрано со склада')
            return True
        else:
            print('Такого оборудования нет')
            return False

    def get_equipment(self, place):
        try:
            if place not in self.equipments.keys():
                raise IsExist('Такого места не существует')
            return self.equipments[place]
        except IsExist as err:
            return err

    @staticmethod
    def get_values(my_dict={}, element=''):
        for i, el in my_dict.items():
            if element == el:
                return i
        return False


class Office_Equipments:

    def __init__(self, type_equipment, cost_equipment):
        self.type_equipment = type_equipment
        self.cost_equipment = cost_equipment


class Printers(Office_Equipments):

    def __init__(self, cost, name):
        super().__init__('Принтер', cost)
        self.name = name

    def __str__(self):
        return (f'{self.name} {self.type_equipment} {self.cost_equipment}')


class Scanners(Office_Equipments):

    def __init__(self, cost, name):
        super().__init__('Сканнер', cost)
        self.name = name

    def __str__(self):
        return (f'{self.name} {self.type_equipment} {self.cost_equipment}')


class CopyMachines(Office_Equipments):

    def __init__(self, cost, name):
        super().__init__('МФУ', cost)
        self.name = name

    def __str__(self):
        return (f'{self.name} {self.type_equipment} {self.cost_equipment}')

my_printer = Printers(10000, 'Для бухгалтерии')
my_scanner = Scanners(15000, 'Для рекламщиков')
my_copymachine = CopyMachines(20000, 'В цех')
my_printer2 = Printers(10000, 'Для ИТ')

print('Выводим оборудование')
print(my_printer)
print(my_scanner)
print(my_copymachine)

my_store = Store()

my_store.add_equipment(1, my_printer)
my_store.add_equipment(2, my_scanner)
my_store.add_equipment(3, my_copymachine)
my_store.add_equipment(1, my_printer2)
print('Выводим склад после добавления')
print(my_store)


my_store.remove_equipment(my_scanner)

print('Выводим склад после удаления')
print(my_store)

print(my_store.get_equipment(0))
