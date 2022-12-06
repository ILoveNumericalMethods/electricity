import numpy

class Vector:
    """    Тип данных, описывающий вектор.    vector - координаты вектора    """    def init (self, x, y):
        """        Конструктор        """        self.vector = numpy.array([x, y])

    def __add__(self, other):

        return self.vector + other.vector

    def __mul__(self, other):

        return numpy.dot(self.vector, other.vector)


    def draw (self):
        """        дописать отрисовку вектора        """
