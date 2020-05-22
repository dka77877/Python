# Реализовать базовый класс Worker ( работник), в котором определить атрибуты: name,
# surname, position ( должность), i ncome ( доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
# дохода с учетом премии ( get_total_income) .

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        full_name = self.name, self.surname
        return ' '.join(full_name)

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


pos = Position('Ivan', 'Petrov', 'manager', 2000, 5000)
print(pos.name, pos.surname, pos.position, pos._income)
print(pos.get_full_name())
print(pos.get_total_income())
