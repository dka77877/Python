# Реализовать класс Road ( дорога), в котором определить атрибуты: l ength ( длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
# для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
# толщины полотна. Проверить работу метода.

class Road:
    def __init__(self, _length, _width):
        self._a = _length
        self._b = _width

    def massa(self):
        print(self._a * self._b * 25 * 5 / 1000, 'т')


r = Road(5000, 20)
r1 = Road(3000, 20)
r.massa()
r1.massa()
