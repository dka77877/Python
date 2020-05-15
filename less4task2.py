# Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
import random

my_list = [random.randint(0, 1000) for i in range(15)]
print('Исходный список;', my_list)
itog = []
for i in range(len(my_list) - 1):
    if my_list[i + 1] > my_list[i]:
        itog.append(my_list[i + 1])
print('Результат:', itog)
