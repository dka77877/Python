# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль

num1 = float(input('Введите делимое: '))
num2 = float(input('Введите делитель: '))

def chastnoe(delimoe, delitel):
    if delitel == 0:
        delitel = float(input('Деление на 0, введите дpугой делитель!  '))
    ch = delimoe / delitel
    return ch

print(chastnoe(num1, num2))
