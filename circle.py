from math import pi

class Circle:
    """
    Circle class
    charge
    x - x-coordinate
    y - y-coordinate
    radius
    """

    def __init__ (self, x, y, radius):
        """
        Constructor
        """
        self.radius = radius
        self.charge = pi * self.radius ** 2
        self.x = x
        self.y = y


