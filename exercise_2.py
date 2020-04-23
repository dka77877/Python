time = int(input('Введите время в сек.'))
hours = time // 3600
min = (time % 3600 // 60)
sec = (time % 60)

print('{0}:{1}:{2}'.format(hours, min, sec))
