# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля i tertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
# завершения.

from itertools import count
from itertools import cycle

def my_gen(first):
    i = 0
    print('Итератор, генерирующий целые числа:')
    for el in count(first):
        if i > 15:
            break
        i += 1
        print(el, end=' ')
    print('\n')

def my_cycle(*args):
    i = 0
    print('Итератор, повторяющий элементы некоторого списка:')
    for el in cycle(args):
        if i > 15 :
            break
        i += 1
        print(el, end=' ')
    print('\n')

my_gen(70)
my_cycle('раз', 'два', 'три')