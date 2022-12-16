from math import pi

class Circle:
    """
    Класс окружности
    charge - заряд
    x - координата по x
    y - координата по y
    radius - радиус
    """

    def __init__ (self, x, y, radius):
        """
        Конструктор
        """
        self.radius = radius
        self.charge = pi * self.radius ** 2
        self.x = x
        self.y = y


