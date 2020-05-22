# Реализовать класс Stationery ( канцелярская принадлежность). Определить в нем атрибут t itle
# (название) и метод draw ( отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen ( ручка), Pencil ( карандаш), Handle ( маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисорвки...')

class Pen(Stationery):
    def draw(self):
        print('Pen drawing...\n')

class Pencil(Stationery):
    def draw(self):
        print('Pencil drawing...\n')

class Handle(Stationery):
    def draw(self):
        print('Handle drawing...\n')

p1 = Pen('Ручка')
p2 = Pencil('Карандаш')
p3 = Handle('Маркер')

print(p1.title)
p1.draw()

print(p2.title)
p2.draw()

print(p3.title)
p3.draw()