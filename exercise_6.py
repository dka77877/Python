a = float(input('Введите результат в первый день, км: '))
b = float(input('Введите требуемый результат, км: '))

if a > b:
    print ('Ты уже молодец!')
else:
    num_days = 1
    while a < b:
        a = a + 0.1 * a
        num_days += 1
    print('Понадобится ', num_days, ' дня(дней)')
