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

    def __eq__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val == other)

    def __ne__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val != other)

    def __lt__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val < other)

    def __le__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val <= other)

    def __gt__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val > other)

    def __ge__(self, other):
        other = self.__check_data(other)
        return MyInt(self.__val >= other)


a = MyInt(5)
print('3' > a)
