class Matrix:
    def __init__(self, param1):
        self.param1 = param1

    def __str__(self):
        for i in range(len(self.param1)):
            my_str = self.param1[i]
            print(my_str)
        print('\n')

    def __add__(self, other):
        my_matr = []
        for el in range(len(self.param1)):
            itog = []
            for i in range(len(self.param1[el])):
                itog.append(self.param1[el][i] + other.param1[el][i])
            my_matr.append(itog)
        return (my_matr)


matrix1 = Matrix([[2, 3, 4, 7], [8, 9, 2, 10], [4, 7, 1,-2]])
matrix1.__str__()
matrix2 = Matrix([[3, 6, 0, -1], [4, 7, 4, 11], [5, 7, -7, 2]])
matrix2.__str__()
matrix_itog = Matrix(matrix1.__add__(matrix2))
matrix_itog.__str__()

