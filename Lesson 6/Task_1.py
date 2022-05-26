# 1. Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.
import time
class TrafficLight:
    _color = ''

    def running(self, state):
        if state == 'RED' and (self._color == 'GREEN' or self._color ==''):
            self._color = 'RED'
            print(f'Lighter state is {self._color}')
            time.sleep(7)
        elif state == 'YELLOW' and (self._color == 'RED'):
            self._color = 'YELLOW'
            print(f'Lighter state is {self._color}')
            time.sleep(2)
        elif state == 'GREEN' and (self._color == 'YELLOW'):
            self._color = 'GREEN'
            print(f'Lighter state is {self._color}')
            time.sleep(5)
        else:
            print('Порядок нарушен')


lighter = TrafficLight()
lighter.running('RED')
lighter.running('YELLOW')
lighter.running('GREEN')
lighter.running('YELLOW')

