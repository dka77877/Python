# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

from random import randint, shuffle


class Card:
    def __init__(self):
        self.my_card = []
        self.my_card_itog = []
        self.nums = []

    def __str__(self):
        return f"Карточка\n{self.my_card_itog[0]}\n{self.my_card_itog[1]}\n{self.my_card_itog[2]}\n"

    def my_create(self):
        i = 0
        el = 0
        while i < 15:
            el = randint(1, 90)
            if el in self.my_card:
                continue
            else:
                self.my_card.append(el)
                i += 1
        my_card_itog = []
        self.my_card_itog.append(sorted(self.my_card[:5]))
        self.my_card_itog.append(sorted(self.my_card[5:10]))
        self.my_card_itog.append(sorted(self.my_card[10:]))
        return self.my_card_itog


class Player(Card):
    def __str__(self):
        return f"Карточка игрока\n{self.my_card_itog[0]}\n{self.my_card_itog[1]}\n{self.my_card_itog[2]}\n"

    def cross_pl(self, num):
        self.num = num
        my_count = 0
        my_all = 0
        for row in self.my_card_itog:
            if self.num in row:
                row[row.index(self.num)] = '-'
                my_count += 1
            my_all += row.count('-')
            if my_all == 15:
                print('Игра окончена! Ты победил!')
                exit(1)
        if my_count == 0:
            print(f'Номера {self.num} у Вас нет. Вы проиграли!')
            exit(1)
        return self.my_card_itog

    def skip_pl(self, num):
        self.num = num
        # if str(self.num) in str(self.my_card_itog):
        for row in self.my_card_itog:
            if self.num in row:
                print(f'Номер {self.num} Вы пропустили. Вы проиграли!')
                exit(1)


class Comp(Card):
    def __str__(self):
        return f"Карточка компьютера\n{self.my_card_itog[0]}\n{self.my_card_itog[1]}\n{self.my_card_itog[2]}\n"

    def cross(self, num):
        self.num = num
        self.my_all = 0
        for row in self.my_card_itog:
            if self.num in row:
                row[row.index(self.num)] = '-'
            self.my_all += row.count('-')
            if self.my_all == 15:
                print('Игра окончена! Компьютер победил!')
                exit(1)
        return self.my_card_itog


class Boch:
    def __init__(self):
        self.my_list = []

    def nums_list(self):
        self.my_list = [i + 1 for i in range(90)]
        shuffle(self.my_list)
        return self.my_list


comp = Comp()
comp.my_create()
print(comp)

pl = Player()
pl.my_create()
print(pl)

b = Boch()
my_tupl = tuple(b.nums_list())
k = 0
while k < 91:  # Объявление очередного номера бочонка
    print(f"Выпал номер {my_tupl[k]}. Осталось бочонков - {89 - k}")
    comp.cross(my_tupl[k])
    print(comp)
    print(pl)
    while True:
        choice = input('Вы зачёркиваете этот номер? Да - нажмите Y; Нет - нажмите N: ')
        if choice == 'Y':
            pl.cross_pl(my_tupl[k])
            break
        elif choice == 'N':
            pl.skip_pl(my_tupl[k])
            break
        else:
            print('Некорректный ввод!')
            continue
    print(pl)
    k += 1
