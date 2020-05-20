# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

f_4_new = open('less5f4_new.txt', 'a', encoding='utf-8')

with open('less5f4.txt', encoding='utf-8') as f_4:
    for line in f_4:
        my_list_line = line.split()
        my_list_line.insert(0, my_dict.get(my_list_line[0]))
        my_list_line.pop(1)
        f_4_new.write(' '.join(my_list_line) + '\n')

f_4_new.close()

