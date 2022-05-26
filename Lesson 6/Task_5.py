# 5. Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    title = ''

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):

    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationery):

    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationery):

    def __init__(self):
        self.title = 'Маркер'

    def draw(self):
        return 'Запуск отрисовки маркером'


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()

print(my_pen.draw())
print(my_pencil.draw())
print(my_handle.draw())
