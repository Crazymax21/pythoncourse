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

    def __init__(self, cells=0):
        self._cells_count = cells
        self._cells_row = 7
        self._cell_struct = []
        self._construct_cell()

    def __add__(self, other):
        return Cell(self._cells_count + other._cells_count)

    def __sub__(self, other):
        if self._cells_count - other._cells_count <= 0:
            raise TypeError('Операция не возможна')
        else:
            return Cell(self._cells_count - other._cells_count)

    def __mul__(self, other):
        return Cell(self._cells_count * other._cells_count)

    def __truediv__(self, other):
        if other._cells_count == 0:
            raise ZeroDivisionError('Операция не возможна')
        else:
            return Cell(self._cells_count // other._cells_count)

    def make_order(self, cell_row):
        self._cells_row = cell_row
        self._construct_cell()

    def _construct_cell(self):
        self._cell_struct.clear()
        cell_parts = self._cells_count / self._cells_row if self._cells_count % self._cells_row == 0 else (
                                                                                                                self._cells_count // self._cells_row) + 1
        for i in range(int(cell_parts)):
            mesh = self._cells_row if self._cells_count - self._cells_row * (
                i) > self._cells_row else self._cells_count - self._cells_row * (i)
            self._cell_struct.append(mesh * '*')

    def __str__(self):
        return '\n'.join(self._cell_struct)


my_cell1 = Cell(7)

my_cell2 = Cell(0)

print('Клетка 1')
print(my_cell1)
print('Клетка 2')
print(my_cell2)

my_cell3 = my_cell1 / my_cell2
my_cell3.make_order(4)
print('Клетка 3')
print(my_cell3)
