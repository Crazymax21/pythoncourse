# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


input_data = input("Введите выражение: ")

input_data = list(map(float, input_data.split('/')))
result = input_data[0]/input_data[1] if input_data[1] != 0 else MyError('На 0 делить нельзя')
print(result)
