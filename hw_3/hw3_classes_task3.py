class MyInt:
    def __init__(self, val):
        self.__val = val

    def __repr__(self):
        return f'{self.__class__}: {self.__val}'

    def __str__(self):
        return str(self.__val)

    @classmethod
    def __check_data(cls, other):
        if type(other) is str:
            other = int(other)
            return other
        elif type(other) is int:
            return other
        else:
            raise TypeError('Данные должны быть строкой или числом')

    def __add__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val + other)

    def __radd__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val + other)

    def __sub__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val - other)

    def __rsub__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val - other)

    def __mul__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val * other)

    def __rmul__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val * other)

    def __truediv__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val / other)

    def __rtruediv__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val / other)
