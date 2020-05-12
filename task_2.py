my_str = input('введите через пробел элементы списка')
my_list = my_str.split()

num = 0
while num < len(my_list):
    el = my_list[num]
    my_list.insert((num + 2), el)
    my_list.pop(num)
    num += 2
print(my_list)
