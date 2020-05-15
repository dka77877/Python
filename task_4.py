my_str = input('введите через пробел элементы списка: ')
my_list = my_str.split()

num = 0
while num < len(my_list):
    el = str(my_list[num])
    print(num + 1, el[:10])
    num += 1
