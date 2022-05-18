# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    _length = 0
    _width = 0
    _weight_unit = 25
    _depth = 5

    def __init__(self, lehgth, width):
        self.set_attr(lehgth, width)

    def set_attr(self, lehgth, width):
        self._length = lehgth
        self._width = width

    def calc_weight(self):
        return f'{self._length}м * {self._width}м * {self._weight_unit}кг * {self._depth}см = {self._length*self._width*self._weight_unit*self._depth} кг'

my_road = Road(5000,20)
print(my_road.calc_weight())
my_road.set_attr(2000, 20)
print(my_road.calc_weight())