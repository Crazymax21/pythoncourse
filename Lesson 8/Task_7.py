# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class Complex:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __str__(self):
        return f'{self.a}+{self.b}i' if self.b >= 0 else f'{self.a}{self.b}i'
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.b * other.a + self.a * other.b
        return Complex(a, b)


my_first_digit = Complex(30, -2)
my_second_digit = Complex(6, 10)

print(my_first_digit)
print(my_second_digit)

my_third_digit = my_first_digit + my_second_digit

print(my_third_digit)

my_fourth_digit = my_first_digit * my_second_digit
print(my_fourth_digit)
