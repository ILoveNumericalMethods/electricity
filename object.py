import numpy
from math import pi
from math import cos
from math import sin
from circle import Circle
from idetify import is_in_figure


class Object:
    """
    Charged body
    mask_array - showing if the point in the object
    x - shift in x from 0
    y - shift in y from 0
    approx_circles - approximation of the body by balls
    priority - priority of access to the object
    """

    def __init__(self, formula, x, y, height, width):
        """
        Constructor
        """

        self.x = x
        self.y = y
        self.mask_array = self.make_mask_array(formula, height, width)
        self.priority = 1
        self.approx_circles = []
        self.make_approximation(height, width, 0, 0)

    def make_mask_array(self, formula, height, width):
        """
        creating array to chech if the point in the object
        """
        mask_array = numpy.zeros((height, width))

        half_of_y = int(height / 2)
        half_of_x = int(width / 2)

        for y in range(-1 * half_of_y, half_of_y):
            for x in range(-1 * half_of_x, half_of_x):
                if is_in_figure(formula, x, y, 0, 0) <= 0:
                    mask_array[y][x] = 1
        return mask_array

    def make_approximation(self, height, width, start_x, start_y):
        """
        The function takes the first step of recursion
        """
        x, y, mass = self.find_center_of_mass(start_x, start_y, width, height)

        if self.is_point_in_unfilled_space(x, y) == True:
            circle = Circle(x - self.x, y - self.y, self.find_radius(x, y, min(width, height)))
            self.approx_circles.append(circle)

        self.recurent_part_of_make_approximation(y, x, start_x, start_y, mass)
        self.recurent_part_of_make_approximation(y, width - x, x, start_y, mass)
        self.recurent_part_of_make_approximation(height - y, x, start_x, y, mass)
        self.recurent_part_of_make_approximation(height - y, width - x, x, y, mass)

        return

    def recurent_part_of_make_approximation(self, heigth, width, start_x, start_y, mass):
        """
        Recursive approximation of the figure with balls
        P is the coverage fraction at which the recursion stops
        """
        P = 0.1 / 4
        x, y, new_mass = self.find_center_of_mass(start_x, start_y, width, heigth)

        if new_mass <= mass * P or new_mass == -1:
            return

        if self.is_point_in_unfilled_space(x, y) == True:
            self.approx_circles.append(Circle(x - self.x, y - self.y, self.find_radius(x, y, min(width, heigth))))

        self.recurent_part_of_make_approximation(y, x, start_x, start_y, mass)
        self.recurent_part_of_make_approximation(y, width - x, x, start_y, mass)
        self.recurent_part_of_make_approximation(heigth - y, x, start_x, y, mass)
        self.recurent_part_of_make_approximation(heigth - y, width - x, x, y, mass)

        return

    def is_point_in_unfilled_space(self, x, y):
        """
        Checking to find a point in a space that has not yet been filled
        """

        x = int(x - self.x)
        y = int(y - self.y)

        if len(self.approx_circles) != 0:
            for current_circle in self.approx_circles:
                if (x - current_circle.x) ** 2 + (y - current_circle.y) ** 2 <= current_circle.radius ** 2:
                    return False

        if self.mask_array[y][x] == 1:
            return True

        return False

    def find_center_of_mass(self, start_x, start_y, distance_of_x, distance_of_y):
        """
        Looks for the centre of mass of the figure in a rectangle with an upper left corner (start_x, start_y) and side
        lengths distance_of_x and distance_of_y
        """
        center_of_mass_x = 0
        center_of_mass_y = 0
        mass = 0
        for x in range(start_x, distance_of_x):
            for y in range(start_y, distance_of_y):
                if self.is_point_in_unfilled_space(x, y) == True:
                    center_of_mass_x += x
                    center_of_mass_y += y
                    mass += 1

        if mass == 0:
            mass = -1

        return int(center_of_mass_x / mass), int(center_of_mass_y / mass), mass

    def find_radius(self, x, y, max_radius):
        """
        Searches for the radius of an inscribed circle
        N - number of tests
        E - accuracy of radius fitting
        """
        N = 100
        E = 0.1

        left = 0
        right = max_radius

        while right - left > E:
            middle = (left + right) / 2

            flag = 0
            for i in range(N):
                if (self.is_point_in_unfilled_space(x + middle * cos(2 * pi * i / N),
                                                    y + middle * sin(2 * pi * i / N)) == True):
                    flag += 1

            if flag != N:
                right = middle
            else:
                left = middle

        return right

    def calculate_potential_in_that_point(self, x, y):
        """
        The function reads the potential at a given point
        K is the normalisation constant
        """
        K = 5

        x = x - self.x
        y = y - self.y

        potential = 0

        for current_circle in self.approx_circles:
            potential += K * current_circle.charge / (
                        ((current_circle.x - x) ** 2 + (current_circle.y - y) ** 2) ** 0.5)
        return potential


class All_objects:
    """
    Class of all objects and working with them
    all_objects - array of objects
    width - screen width
    height - screen height
    """

    def __init__(self, height, width, y, x):
        """
        Constructor
        """
        self.height = height
        self.width = width
        self.all_objects = []
        self.y = y
        self.x = x

    def find_best_object(self, x, y):
        """
        Searches for the object with the highest priority
        """

        index_of_best_priority = -1
        best_priority = 1e9
        for index in range(len(self.all_objects)):

            index_of_best_priority = -1

            if self.all_objects[index].mask_array[(-1) * self.y + y - self.all_objects[index].y][
                (-1) * self.x + x - self.all_objects[index].x] == 1 \
                    and self.all_objects[index].priority < best_priority:
                index_of_best_priority = index
                best_priority = self.all_objects[index].priority

        return index_of_best_priority

    def add_object(self, formula, x, y):
        """
        Adding an object to an array
        """
        self.all_objects.append(Object(formula, x, y, self.height, self.width))

        for current_object in self.all_objects:
            current_object.priority += 1

    def delete_object(self, x, y):
        """
        Deleting an object from an array
        """
        if self.find_best_object(x, y) != -1:
            self.all_objects.pop(self.find_best_object(x, y))

    def move_object(self, x_from, y_from, x_to, y_to):
        """
        Moving an object
        """
        index = self.find_best_object(x_from, y_from)
        if index != -1:
            self.all_objects[index].x += x_to - x_from
            self.all_objects[index].y += y_to - y_from

            self.all_objects[index].priority = 0
            for current_object in self.all_objects:
                current_object.priority += 1

    def make_scalar_field(self):
        """
        Constructing a scalar field
        """
        scalar_field = numpy.empty((self.height, self.width))
        max_potential = 0

        for y in range(self.height):
            for x in range(self.width):
                potential = 0

                for current_object in self.all_objects:
                    if current_object.mask_array[y - current_object.y][x - current_object.x] == 1:
                        potential = -1
                        break

                for current_object in self.all_objects:

                    if potential != -1:
                        potential += current_object.calculate_potential_in_that_point(x, y)

                scalar_field[y][x] = potential
                max_potential = max(max_potential, potential)

        return scalar_field, max_potential
