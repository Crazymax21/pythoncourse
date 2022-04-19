# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#finish
user_number = int(input('Введите число: '))

user_max = user_number%10

while user_number != 0:
    if user_max <= user_number%10:
        user_max = user_number%10
    user_number = user_number // 10

print(f'Самая большая цифра: {user_max}')