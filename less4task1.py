from sys import argv

my_list1 = argv[1:]


def itog(my_list):
    zp = int(my_list[0]) * int(my_list[1]) + int(my_list[2])
    return zp


print(itog(my_list1))
