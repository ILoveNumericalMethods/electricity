
class Vector:
    """
    Тип данных, описывающий вектор.
    x_end - x кооридината конца вектора
    y_end - y кооридината конца вектора
    x_begin - x кооридината начала вектора
    y_begin - y кооридината начала вектора
    """

    def __init__ (self, x_begin, y_begin, x_end, y_end):
        """
        Конструктор
        """
        self.x_begin = x_begin
        self.y_begin = y_begin
        self.x_end = x_end
        self.y_end = y_end

    def __add__(self, other):
        vector = Vector(0, 0, 0, 0)

        vector.x_begin = self.x_begin
        vector.y_begin = self.y_begin
        vector.x_end = self.x_end + other.x_end - other.x_begin
        vector.x_end = self.y_end + other.y_end - other.y_begin

        return vector

    def __add__(self, other):
        vector = Vector(0, 0, 0, 0)

        vector.x_begin = self.x_begin
        vector.y_begin = self.y_begin
        vector.x_end = self.x_end + other.x_end - other.x_begin
        vector.x_end = self.y_end + other.y_end - other.y_begin

        return vector

    def __mul__(self, other):
        vector = Vector(0, 0, 0, 0)

        vector.x_begin = self.x_begin
        vector.y_begin = self.y_begin
        vector.x_end = self.x_end * other
        vector.x_end = self.y_end * other

        return vector


    def dot_product(self, vector):
        """
        скаларное поизведение
        """
        return (self.x_end - self.x_begin) * (vector.x_end - vector.x_begin) + (self.y_end - self.y_begin) * (vector.y_end - vector.y_begin)

    def draw (self):
        """
        дописать отрисовку вектора
        """
