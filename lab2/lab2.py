from sympy import diff


class FindMin:
    __first_diff = str
    __second_dif = str

    def function(self, x):
        return int(x*x + 2)

    def get_diff(self, func):
        self.__first_diff = diff(func)
        self.__second_diff = diff(self.__first_diff)
        print("Первая производная " + self.__first_diff)
        print("Вторая производная " + self.__second_diff)

    def find_minimum(self):
        for char in self.__first_diff:
            if char == 'x':

        pass


if __name__ == "__main__":
    find_min = FindMin()
    print('y(x) = ')
    y = input()
    find_min.get_diff(y)
