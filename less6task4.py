# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, i s_police ( булево). А также методы: go, stop, t urn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# ( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('go...')

    def stop(self):
        print('stop...')

    def turn(self, direction):
        print('turn', direction)

    def show_speed(self):
        print('Скорость = ', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Скорость: ', self.speed if self.speed <= 60 else str(self.speed) + ' Превышение скорости!')


class WorkCar(Car):
    def show_speed(self):
        print('Скорость: ', self.speed if self.speed <= 40 else str(self.speed) + ' Превышение скорости!')


class SportCar(Car):
    pass

class PoliceCar(Car):
    pass





auto = TownCar(70, 'red', 'mazda', False)
print(auto.speed)
print(auto.color)
print(auto.name)
print(auto.is_police)
auto.turn('left')
auto.show_speed()
print('\n')

auto1 = WorkCar(35, 'white', 'ford', False)
print(auto1.speed)
print(auto1.color)
print(auto1.name)
print(auto1.is_police)
auto1.go()
auto1.turn('left')
auto1.show_speed()
print('\n')

auto2 = PoliceCar(90, 'yellow', 'bmw', True)
print(auto2.speed)
print(auto2.color)
print(auto2.name)
print(auto2.is_police)
auto2.go()
auto2.turn('left')
auto2.show_speed()
print('\n')
