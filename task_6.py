my_prod = []
a = 0
n = 1
while a == 0:
    my_pr = []
    my_tovar = {"название": input('Введите название товара: '), "цена": input('Введите цену товара: '),
                "количество": input('Введите количество товара: '), "ед": input('Введите ед. измерения товара: ')}
    my_pr.append(n)
    my_pr.append(my_tovar)
    my_prod.append(tuple(my_pr))
    n += 1
    a = input('Если хотите добавить ещё один товар, нажмите 0 ')
    try:
        a = int(a)
    except:
        a = 1

my_dict = {}
for key in my_prod[0][1].keys():
    my_vol = []
    my_index = 0
    while my_index < len(my_prod):
        my_vol.append(my_prod[my_index][1].get(key))
        my_index += 1
    my_dict[key] = (list(set(my_vol)))

print(my_dict)
