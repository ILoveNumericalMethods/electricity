import numpy
from vector import Vector
import mapping

e_vectors = numpy.array([Vector(0, 0), Vector(0, 1), Vector(1, 1), Vector(1, 0), Vector(1, -1), Vector(0, -1), Vector(-1, -1), Vector(-1, 0), Vector(-1, 1)])

standart_coefficient_array = numpy.array([1 / 3, 1 / 18, 1 / 36, 1 / 18, 1 / 36, 1 / 18, 1 / 36, 1 / 18, 1 / 36])

class Node:
    """    
    узел расчетной ячейки    
    направления нумерются с центрального, далее верхний и по часовой стреке    
    macro_velocity - вектор скорости   
    micro_velocity_array - массив скоростей по направлениям - строка
    coefficient_array - коэффициенты напрвлений - диагональная матрица    
    Boltzmann_function -  функцией распределения плотности вероятности частиц по координатам и по скоростям - строка
    distribution_function - равновесная функция распределения - строка
    density - плотность жидкости    
    """   
    
    def __init__(self, macro_velocity, micro_velocity_array, coefficient_array, Boltzmann_function, distribution_function, density):
        """        
        Конструктор        
        """        
        self.macro_velocity = macro_velocity
        self.micro_velocity_array = micro_velocity_array
        self.coefficient_array = coefficient_array
        self.Boltzmann_function = Boltzmann_function
        self.distribution_function = distribution_function
        self.density = density

    def calculate_Boltzmann_function_around(self, tau):
        """        
        расчитаывает приращения функций Больтсмана для каждой частицы вокруг данной        
        """

        return -1 * (self.Boltzmann_function - self.distribution_function) / tau

    def calculate_density (self):
        """        
        считает плотность        
        """        
        self.density = numpy.sum(self.Boltzmann_function)

    def calculate_macro_velocity (self):
        """        
        считает скорость        
        """
        for i in range(9):
            self.macro_velocity += e_vectors[i] % (self.micro_velocity_array[i] * self.Boltzmann_function[i] / self.density)

    def calculate_distribution_function (self, R, T):
        """        
        расчитаывает функцию по направлению        
        """        
        self.distribution_function = numpy.arange(9)

        self.distribution_function = (1 + (e_vectors[self.distribution_function] * self.macro_velocity) / (R * T)
                                      + (e_vectors[self.distribution_function] * self.macro_velocity) ** 2 / (2 * (R * T) ** 2)
                                      - self.macro_velocity * self.macro_velocity / (2 * R * T))

        self.distribution_function *= self.density

        self.distribution_function = self.coefficient_array * self.distribution_function

    def calculate_Boltzmann_function_in_this_node (self, tau):
        """        
        расчитаывает функций Больтсмана в узле        
        """        

        self.Boltzmann_function = self.Boltzmann_function - (self.Boltzmann_function - self.distribution_function) / tau


class Grid:
    """    
    Расчетная сетка    
    object - объект    
    length - длина трубы    
    width - толщина трубы        
    start_velocity - начальная скорость течения    
    grid - сетка    
    density - плотность
    R - универсальчная газовая постоянная
    T - температура
    t - параметр
    """

    def __init__ (self, length, width, object, density, R, T, t):

        grid_map = mapping.made_map(length, width, object)

        self.grid = [[Node(Vector(0, 0), numpy.zeros(9), standart_coefficient_array, numpy.zeros(9), numpy.zeros(9), density)] * (width + 2)] * (length + 2)

        for i in range(length + 2):
            for j in range(width + 2):
                if (grid_map[i][j] == 1):
                    self.grid[i][j].coefficient_array = numpy.zeros(9)

                self.grid[i][j].coefficient_array = mapping.make_coefficient_array(grid_map, length, width, i, j)



        self.object = object
        self.length = length
        self.width = width
        self.density = density
        self.R = R
        self.T = T
        self.t = t

    def modeling(self, output_file):

        for j in range(self.width):
            self.grid[1][j + 1].macro_velocity = Vector(0.1, 0)
            self.grid[1][j + 1].micro_velocity_array = numpy.array([0, 0.1, 0, 0, 0, 0, 0, 0, 0])
            self.grid[1][j + 1].Boltzmann_function = numpy.array([0, 1, 0, 0, 0, 0, 0, 0, 0])
            self.grid[1][j + 1].calculate_distribution_function(self.R, self.T)
            self.grid[1][j + 1].density = self.density

            """
            self.grid[self.length + 1][j + 1].macro_velocity = Vector(0, 0)
            self.grid[self.length + 1][j + 1].micro_velocity_array = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.grid[self.length + 1][j + 1].Boltzmann_function = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.grid[self.length + 1][j + 1].calculate_distribution_function(self.R, self.T)
            self.grid[self.length + 1][j + 1].density = self.density
            """




        for i in range(self.length):
            for j in range(self.width):

                delta_f = self.grid[i + 1][j + 1].calculate_Boltzmann_function_around(self.t)
                print(delta_f)

                self.grid[i + 1][j + 1].Boltzmann_function[0] = delta_f[0]
                self.grid[i + 2][j + 1].Boltzmann_function[1] = delta_f[1]
                self.grid[i + 2][j + 2].Boltzmann_function[2] = delta_f[2]
                self.grid[i + 1][j + 2].Boltzmann_function[3] = delta_f[3]
                self.grid[i][j + 2].Boltzmann_function[4] = delta_f[4]
                self.grid[i][j + 1].Boltzmann_function[5] = delta_f[5]
                self.grid[i][j].Boltzmann_function[6] = delta_f[6]
                self.grid[i + 1][j].Boltzmann_function[7] = delta_f[7]
                self.grid[i + 2][j].Boltzmann_function[8] = delta_f[8]

        for i in range(self.length):
            for j in range(self.width):
                self.grid[i + 1][j + 1].calculate_density()
                self.grid[i + 1][j + 1].calculate_macro_velocity()
                self.grid[i + 1][j + 1].calculate_distribution_function(self.R, self.T)
                self.grid[i + 1][j + 1].calculate_Boltzmann_function_in_this_node(self.t)

    def print_data(self, output_file):

        for i in range(self.length):
            for j in range(self.width):
                output_file.write(str(self.grid[i + 1][j + 1].macro_velocity.vector[0]) + " " + str(self.grid[i + 1][j + 1].macro_velocity.vector[1]) + " ")

            output_file.write("\n")

        output_file.write("\n")
    """
        with open(output_filename, 'w') as output_file:
            for i in range(self.length):
                for j in range(self.width):
                    print(output_file, self.grid[i + 1][j + 1].macro_velocity, end=' ')
                
                print()

        print()
        print()
    """
