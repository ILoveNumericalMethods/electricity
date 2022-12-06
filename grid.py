import numpy
import Vector

e_vectors = numpy.array([Vector(0, 0), Vector(0, 1), Vector(1, 1), Vector(1, 0), Vector(1, -1), Vector(0, -1), Vector(-1, -1), Vector(-1, 0), Vector(-1, 1)])

class Node:
    """    узел расчетной ячейки    направления нумерются с центрального, далее верхний и по часовой стреке    macro_velocity - вектор скорости    micro_velocity_array - массив скоростей по направлениям - строка    coefficient_array - коэффициенты напрвлений - диагональная матрица    Boltzmann_function -  функцией распределения плотности вероятности частиц по координатам и по скоростям - столбец    distribution_function - равновесная функция распределения - столбец    density - плотность жидкости    """    def __init__ (self, macro_velocity, micro_velocity_array, coefficient_array, Boltzmann_function, distribution_function, density):
        """        Конструктор        """        self.macro_velocity = macro_velocity
        self.micro_velocity_array = micro_velocity_array
        self.coefficient_array = coefficient_array
        self.Boltzmann_function = Boltzmann_function
        self.distribution_function = distribution_function
        self.density = density

    def calculate_Boltzmann_function_around (self, node, tau):
        """        расчитаывает приращения функций Больтсмана для каждой частицы вокруг данной        """        return -1 * (self.Boltzmann_function - self.distribution_function) / tau

    def calculate_decity (self):
        """        считает плотность        """        self.density = numpy.sum(self.Boltzmann_function)

    def calculate_macro_velocity (self):
        """        считает скорость        """        self.macro_velocity += self.micro_velocity_array * self.Boltzmann_function

        self.micro_velocity_array /= self.density

    def calculate_distribution_function (self, R, T):
        """        расчитаывает функцию по направлению        """        self.distribution_function = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

        self.distribution_function = (1 + (e_vectors[self.distribution_function] * self.macro_velocity) / (R * T)
                                      + (e_vectors[self.distribution_function] * self.macro_velocity) ** 2 / (2 * (R * T) ** 2)
                                      - self.macro_velocity * self.macro_velocity / (2 * R * T))

        self.distribution_function *= self.density
        self.distribution_function = self.coefficient_array * self.distribution_function

    def calculate_Boltzmann_function_in_this_node (self, tau):
        """        расчитаывает функций Больтсмана в узле        """        self.Boltzmann_function -= (self.Boltzmann_function - self.distribution_function) / tau


class greed:
    """    Расчетная сетка    object - объект    length - длина трубы    width - толщина трубы    space_step - пространственный шаг    start_velocity - начальная скорость течения    grid - сетка    """
