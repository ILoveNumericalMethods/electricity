from math import pi
from math import cos
from math import sin
from circle import Circle
from idetify import is_in_figure

class Object:
    """
    Заряженное тело
    formula - формула, задающая форму
    x - смещение по x от 0
    y - смещение по y от 0
    approx_circles - приближение тела шарами
    priority - приооритет доступа к объекту 
    """

    def __init__ (self, formula, x, y, width, heigth):
        """
        Конструктор
        """
        self.formula = formula
        self.x = x
        self.y = y
        self.priority = 1
        self.make_approximation(heigth, width, 0, 0)


    def make_approximation (self, heigth, width, start_x, start_y):
        """
        Функция делает первый шаг рекурсии
        """
        x, y, mass = self.find_сenter_of_mass(start_x, start_y, width, heigth)
        
        if (self.is_point_in_unfilled_space(x, y) == 1):
            self.approx_circles.append(Circle(x, y, self.find_radius(x, y, min(width, heigth))))

        self.recurent_part_of_make_approximation(y, x, start_x, start_y, mass)
        self.recurent_part_of_make_approximation(y, width - x, x, start_y, mass)
        self.recurent_part_of_make_approximation(heigth - y, x, start_x, y, mass)
        self.recurent_part_of_make_approximation(heigth - y, width - x, x, y, mass)

        return

    def recurent_part_of_make_approximation (self, heigth, width, start_x, start_y, mass):
        """
        Рекрсивное приближение фигруы шарами
        P - доля покрытия при котором остановтся рекурсия
        """
        P = 0.95
        x, y, new_mass = self.find_сenter_of_mass(start_x, start_y, width, heigth)
        
        if(new_mass <= mass * P):
            return

        if (self.is_point_in_unfilled_space(x, y) == 1):
            self.approx_circles.append(Circle(x, y, self.find_radius(x, y, min(width, heigth))))

        self.recurent_part_of_make_approximation(y, x, start_x, start_y, mass)
        self.recurent_part_of_make_approximation(y, width - x, x, start_y, mass)
        self.recurent_part_of_make_approximation(heigth - y, x, start_x, y, mass)
        self.recurent_part_of_make_approximation(heigth - y, width - x, x, y, mass)
        
        return

    
    def is_point_in_unfilled_space (self, x, y):
        """
        Проверка нахожднеия точки в еще не заполненом прострастве
        """
        x = x - self.x
        y = y - self.y
        if ((is_in_figure(self.formula, x, y)) != 1):
            return 0

        for current_circle in self.approx_circles:
            if ((x - current_circle.x) ** 2 + (y - current_circle.y) ** 2 <= current_circle.radius ** 2):
                return 0
        
        return 1
    
        
    def find_сenter_of_mass (self, start_x, start_y, distance_of_x, distance_of_y):
        """
        Ищет центр масс фигруы в прямоуголькике с левым верхним углом (start_x, start_y) и длинами сторон distance_of_x и distance_of_y
        """
        сenter_of_mass_x = 0
        сenter_of_mass_y = 0
        mass = 0
        for x in range(start_x, distance_of_x):
            for y in range(start_y, distance_of_y):
                if ((is_in_figure(self.formula, x + self.x, y - self.y)) == 1):
                    сenter_of_mass_x += x
                    сenter_of_mass_y += y
                    mass += 1
        return сenter_of_mass_x / mass, сenter_of_mass_y / mass, mass


    def find_radius (self, x, y, max_radius):
        """
        Ищет радиус вписанной окуржности
        N - количество проверок
        E - точность подбора радиуса
        """
        N = 100
        E = 0.1

        left = 0
        right = max_radius
        
        while (right - left > E):
            middle = (left + right) / 2
            
            flag = 0
            for i in range(N):
                if (self.is_point_in_unfilled_space(x + middle * cos(2 * pi * i / N), y + middle * sin(2 * pi * i / N)) == 1):
                    flag += 1
            
            if (flag == N):
                left = middle
            else:
                right = middle
        
        return right


    def calculate_potential_in_that_point (self, x, y):
        """
        Функция считатет потнциал в указанной точке 
        K - нормировочная постоянная
        """
        K = 1
        
        x = x - self.x
        y = y - self.y

        potential = 0

        for current_circle in self.approx_circles:
            potential += K * current_circle.charge / (((current_circle.x - x) ** 2 + (current_circle.y - y) ** 2) ** 0.5)
        
        return potential
    

class All_objects:
    """
    Все объекты и работа с ними
    all_objects - массив объектов
    width - ширина экрана
    height - высота экрана
    """
    def __init__ (self, height, width):
        """
        Конструктор
        """
        self.height = height
        self.width = width
        self.all_objects = []


    def find_best_object (self, x, y):
        """
        Ищет объект с наивысшим приоритетом
        """
        for index in range(len(self.all_objects)):
            best_priority = 1e9
            index_of_dest_priority = -1
            if (is_in_figure(self.all_object[index].formula, x - self.all_object[index].x, y + self.all_object[index].y) == 1 and self.all_object[index].priority < best_priority):
                index_of_dest_priority = index
                best_priority = self.all_object[index].priority
        
        return index_of_dest_priority
               

    def add_object (self, formula, x, y):
        """
        Добавление объекта в массив
        """
        self.all_objects.append(Object(formula, x ,y, self.width, self.height))
        
        for current_object in self.all_objects:
            current_object.priority += 1

    def delete_object (self, x, y):
        """
        Удаление объекта из масива
        """       
        if (self.find_best_object(x, y) != -1):
            self.all_objects.pop(self.find_best_object(x, y))

        
    def move_object (self, x_from, y_from, x_to, y_to):
        """
        Перемещение объекта
        """
        index = self.find_best_object(x_from, y_from)
        if (index != -1):
            self.all_objects[index].x += x_to - x_from 
            self.all_objects[index].y += y_to - y_from
            
            self.all_objects[index].priority = 0
            for current_object in self.all_objects:
                current_object.priority += 1
    
    def make_scalar_field (self, output_file):
        """
        Построение скалярного поля
        """
        for y in range(self.height):
            for x in range(self.width):
                potential = 0

                for current_object in self.all_objects:
                    
                    if (is_in_figure(current_object.formula, x - current_object.formula.x, y + current_object.formula.y) == 1):
                        output_file.write("-1 ")
                        break

                    potential += current_object.calculate_potential_in_that_point(x, y)
                
                output_file.write(str(potential) + " ")

            output_file.write("\n")