# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go_car(self):
        return 'Машина поехала'

    def stop_car(self):
        return 'Машина остановилась'

    def turn_car(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.speed}'

    def set_speed(self, speed):
        self.speed = speed

class TownCar(Car):

    def __init__(self, name, color, speed):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость превышена'
        else:
            return f'Текущая скорость автомобиля {self.speed}'

class SportCar(Car):

    def __init__(self, name, color, speed):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = False

class WorkCar(Car):
    def __init__(self, name, color, speed):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость превышена'
        else:
            return f'Текущая скорость автомобиля {self.speed}'

class PoliceCar(Car):

    def __init__(self, name, color, speed):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = True


my_car = WorkCar('Lexus', 'Black', 130)
my_car2 = WorkCar('Lexus', 'Green', 40)

my_car.set_speed(20)
print(my_car.show_speed())
print(my_car.go_car())
print(my_car.turn_car('на лево'))
print(my_car.stop_car())
my_car.speed = 120
print(my_car.show_speed())
print(my_car2.show_speed())

