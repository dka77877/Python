# Создать класс TrafficLight ( светофор) и определить у него один атрибут color ( цвет) и метод
# running ( запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.

class TrafficLight:
    __color = 1

    def running(self):
        my_color = {1: 'red - 7сек.', 2: 'yellow - 2сек.', 3: 'green - 5сек.'}
        print(my_color.get(self.__color))
        if self.__color < 3:
            self.__color += 1
        else:
            self.__color = 1


tl = TrafficLight()

tl.running()
tl.running()
tl.running()
tl.running()
tl.running()
tl.running()