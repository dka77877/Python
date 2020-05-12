# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

# person = {'name': input('Имя: '), 'surname': input('Фамилия: '), 'year': input('Город: ')}


def person(name, surname, year, city, email, tel):
    print(name, surname, year, city, email, tel)


person(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    year=input('Год рождения: '),
    city=input('Город: '),
    email=input('E-mail: '),
    tel=input('Телефон: ')
)
