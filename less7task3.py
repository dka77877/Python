class Cell:
    def __init__(self, pc):
        self.pc = pc

    def __add__(self, other):
        pc_new = self.pc + other.pc
        return pc_new

    def __sub__(self, other):
        pc_new = self.pc - other.pc if self.pc > other.pc else 'Отрицательный результат'
        return pc_new

    def __mul__(self, other):
        pc_new = self.pc * other.pc
        return pc_new

    def __truediv__(self, other):
        pc_new = self.pc // other.pc
        return pc_new

    def make_order(self, row_length):
        self.rl = row_length
        self.l = self.pc // self.rl
        my_str = ''
        i = 0
        while i < self.l:
            my_str += '*' * self.rl + '\n'
            i += 1
        my_str += '*' * (self.pc % self.rl)
        return my_str
        # print('*' * (self.pc % self.rl))

cell_1 = Cell(50)
cell_2 = Cell(35)
cell_new = Cell(1)
cell_new.pc = cell_1.__add__(cell_2)
print(cell_new.pc)
cell_new.pc = cell_1.__sub__(cell_2)
print(cell_new.pc)
# cell_new.pc = cell_1.__mul__(cell_2)
# print(cell_new.pc)
# cell_new.pc = cell_1.__truediv__(cell_2)
# print(cell_new.pc)
print([cell_new.make_order(4)])
