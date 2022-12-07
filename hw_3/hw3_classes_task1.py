import math


class Derivative:
    def __init__(self, func):
        self.__func = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__func(x + dx) - self.__func(x)) / dx


@Derivative
def sin_(x):
    return math.sin(x)
