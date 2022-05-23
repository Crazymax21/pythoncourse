# 3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# © geekbrains.ru 20
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n*****.

class Cell:

    def __init__(self, cells):
        self.cells_count = cells
        self._cells_row = 7
        self._cell_struct = []
        self._construct_cell()

    def __add__(self, other):
        self.cells_count += other.cells_count
        self._construct_cell()

    def __sub__(self, other):
        if self.cells_count - other.cells_count <= 0:
            print('Операция не возможна')
        else:
            self.cells_count -= other.cells_count
            self._construct_cell()

    def __mul__(self, other):
        self.cells_count *= other.cells_count
        self._construct_cell()

    def __truediv__(self, other):
        self.cells_count = self.cells_count // other.cells_count
        self._construct_cell()

    def make_order(self, cell_row):
        self._cells_row = cell_row
        self._construct_cell()

    def _construct_cell(self):
        self._cell_struct.clear()
        cell_parts = self.cells_count / self._cells_row if self.cells_count % self._cells_row == 0 else (
                                                                                                                self.cells_count // self._cells_row) + 1
        for i in range(int(cell_parts)):
            mesh = self._cells_row if self.cells_count - self._cells_row * (
                i) > self._cells_row else self.cells_count - self._cells_row * (i)
            self._cell_struct.append(mesh * '*')

    def __str__(self):
        print('\n'.join(self._cell_struct))


my_cell1 = Cell(16)

my_cell2 = Cell(18)

print('Клетка 1')
my_cell1.__str__()
print('Клетка 2')
my_cell2.__str__()

# my_cell1.make_order(3)
#
# print('Клетка 1')
# my_cell1.__str__()
# print('Клетка 2')
# my_cell2.__str__()

# my_cell1.__add__(my_cell2)
# my_cell2.__add__(my_cell1)
my_cell1.__sub__(my_cell2)
#my_cell1.__truediv__(my_cell2)
# my_cell1.__mul__(my_cell2)
print('Клетка 1')
my_cell1.__str__()
print('Клетка 2')
my_cell2.__str__()
