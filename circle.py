from math import pi

class Circle:
    """
    ����� ����������
    charge - �����
    x - ���������� �� x
    y - ���������� �� y
    radius - ������
    """

    def __init__ (self, x, y, radius):
        """
        �����������
        """
        self.radius = radius
        self.charge = pi * self.radius ** 2
        self.x = x
        self.y = y


