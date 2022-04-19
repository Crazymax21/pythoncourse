#2. Пользователь вводит время в секундах.
#Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
#finish
user_time_seconds = int(input('Введите время в секундах: '))

hours = user_time_seconds//60//60
minutes = user_time_seconds//60-(hours*60)
seconds = user_time_seconds-((hours*60+minutes)*60)

print(f'Время в формате чч:мм:сс {hours}:{minutes}:{seconds}')
