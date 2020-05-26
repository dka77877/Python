from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def tissue(self, x):
        pass


class Coat(Clothes):
    def tissue(self, V):
        print(f"Расход = {(V / 6.5 + 0.5):.2f}")


class Suit(Clothes):
    # @property
    def tissue(self, H):
        self.h = H
        self.my_sum = 2 * self.h + 0.3
        print(f"Расход = {self.my_sum:.2f}")
        return self.my_sum

    @property
    def itog(self):
        print( f"Кол-во ткани на 10 костюмов = {self.my_sum * 10}")


a = Coat()
a.tissue(54)
b = Suit()
b.tissue(1.64)
b.itog