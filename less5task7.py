# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать .
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
import json

with open('less5f7.txt', encoding='utf-8') as f_7:
    my_dict = {}
    my_profit = 0
    my_list = []
    for line in f_7.readlines():
        my_profit = float(line.split()[2]) - float(line.split()[3])
        if my_profit > 0:
            my_list.append(my_profit)
        my_dict[line.split()[0]] = my_profit
my_dict_ap = {'average_profit': sum(my_list) / len(my_list)}
my_itog = [my_dict, my_dict_ap]

with open('less5j7.json', 'w', encoding='utf-8') as j_7:
    json.dump(my_itog, j_7)
