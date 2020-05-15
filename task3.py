# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    my_sum = max(my_list)
    my_list.remove(max(my_list))
    my_sum = my_sum + max(my_list)
    return my_sum


print(my_func(2, 5, 8))
