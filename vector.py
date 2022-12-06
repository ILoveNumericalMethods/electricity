import numpy

class Vector:
    """
    Тип данных, описывающий вектор.
    vector - координаты вектора
    """
    def __init__(self, x, y):
        """
        Конструктор
        """
        self.vector = numpy.array([x, y])

    def __add__(self, other):

        ans = self.vector + other.vector
        return Vector(ans[0], ans[1])

    def __mul__(self, other):

        return numpy.dot(self.vector, other.vector)

    def __mod__(self, other):

        return Vector(self.vector[0] * other, self.vector[1] * other)


    def draw (self):
        """        дописать отрисовку вектора        """
