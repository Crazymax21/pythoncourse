# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property
from abc import ABC, abstractmethod


class Clothes(ABC):
    name = ''
    units = []

    def add_unit(self, unit):
        self.units.append(unit)

    @abstractmethod
    def requrement(self):
        pass

    def __str__(self):
        return self.name

    @property
    def calc_requrements(self):
        total = 0
        for el in self.units:
            print(f'Для {el.name} требуется {el.requrement()} ткани')
            total += el.requrement()
        return f'Всего требуется {total} ткани'


class Coat(Clothes):
    size = 0

    def __init__(self, size):
        self.name = 'Пальто'
        self.size = size
        super().add_unit(self)

    def requrement(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    height = 0

    def __init__(self, height):
        self.name = 'Костюм'
        self.height = height
        super().add_unit(self)

    def requrement(self):
        return 2 * self.height + 0.3


coat1 = Coat(65)
suit1 = Suit(20)

print(coat1)
print(coat1.requrement())

print(suit1)

print(Clothes.units)
print(coat1.calc_requrements)
