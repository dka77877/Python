n = input('Введите число ')

i = 9
z = 0
dig = 0

while dig < i:
    if z < len(n):
        dig = int(int(n) // (10 ** z)) % 10
# проверка        print('dig', dig, ' i', i)
        z += 1
    else:
        z = 0
        i += -1
print('Максимальная цифра: ', i)
