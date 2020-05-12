plus = float(input('Введите выручку '))
minus = float(input('Ведите издержки'))

if plus < minus:
    print('Убыток')
else:
    print('Прибыль')
    print('Рентабельность: ', '{:.2f}'.format((plus - minus) / plus * 100), '%')
    worker = int(input('Введите количество сотрудников: '))
    print('Прибыль на одного сотрудника: ', '{:.2f}'.format((plus - minus)  / worker ))
