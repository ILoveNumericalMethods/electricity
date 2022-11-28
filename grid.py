
class Node:
    """
    узел расчетной ячейки
    направления нумерются с центрального, далее верхний и по часовой стреке
    macro_velocity - вектор скорости
    micro_velocity_array - массив скоростей по направлениям
    coefficient_array - коэффициенты напрвлений
    Boltzmann_function -  функцией распределения плотности вероятности частиц по координатам и по скоростям
    distribution_function - равновесная функция распределения
    density - плотность жидкости
    """

    def __init__ (self, macro_velocity, micro_velocity_array, coefficient_array, Boltzmann_function, distribution_function, density):
        """
        Конструктор
        """
        self.macro_velocity = macro_velocity
        self.micro_velocity_array = micro_velocity_array
        self.coefficient_array = coefficient_array
        self.Boltzmann_function = Boltzmann_function
        self.distribution_function = distribution_function
        self.density = density

    def calculate_Boltzmann_function_in_one_direction (self, node, direction, tau):
        """
        расчитаывает функцию по направлению direction
        """
        node.Boltzmann_function[direction] -= (node.Boltzmann_function[direction] - self.coefficient_array[direction] * self.distribution_function[direction]) / tau

    def calculate_decity (self):
        self.density = 0
        for direction in range(9):
            self.density += self.Boltzmann_function[direction]

    def calculate_macro_velocity (self):
        self.macro_velocity = 0
        for direction in range(9):
            self.macro_velocity += self.micro_velocity_array[direction] * self.Boltzmann_function[direction]

        self.micro_velocity_array /= self.density

    def calculate_distribution_function_in_one_direction (self, node, direction, tau):
        """
        расчитаывает функцию по направлению direction
        """
        node.Boltzmann_function[direction] -= (node.Boltzmann_function[direction] - self.distribution_function[direction]) / tau

    def calculate_distribution_function_in_one_direction (self, R, T, e_vectors):
        """
        расчитаывает функцию по направлению direction
        """
        for direction in range(9):
            node.distribution_function[direction] = self.coefficient_array[direction] * self.density * (1 + self.macro_velocity.dot_product)

        self.micro_velocity_array /= self.density

