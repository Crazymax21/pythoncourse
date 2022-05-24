# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Date:
    _day = 0
    _month = 0
    _year = 0

    def __init__(self, date_str):
        self.extract_date(date_str)

    @classmethod
    def extract_date(cls, date_str=''):
        date_list = list(map(int, date_str.split('-')))
        if cls.validate(date_list[1], date_list[2]):
            cls._day = date_list[0]
            cls._month = date_list[1]
            cls._year = date_list[2]

    @staticmethod
    def validate(month, year):
        if 1 <= month <= 12:
            if 1900 <= year <= 3000:
                return True
            else:
                raise TypeError('Год не попадает в промежуток от 1900 до 3000')
        else:
            raise TypeError('Месяц не попадает в промежуток от 1 до 12')

    def __str__(self):
        return f'{self._day}/{self._month}/{self._year}'


date_str = '01-13-2000'

my_date = Date(date_str)

print(my_date)