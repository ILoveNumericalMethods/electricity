import numpy

standart_coefficient_array = numpy.array([1 / 36, 1 / 18, 1 / 36],
                                         [1 / 18, 1 / 3, 1 / 18],
                                         [1 / 36, 1 / 18, 1 / 36])

def made_map (length, width, object):
    
    grid_map = [[0] * width + 2] * length + 2

    center_y = int(width / 2 + 1)
    center_x = int(length / 2 + 1)

    for i in range(length):
        grid_map[0][i] = 1
        grid_map[width + 1][i] = 1
    
    if (object.type == "circle"):
        for i in range(length):
            for j in range(width):
                if((i - center_x) ** 2 + (j - center_y) ** 2 <= object.radius):
                    grid_map[j][i] = 1
    elif (object.type == "square"):
        for i in range(length):
            for j in range(width):
                if(abs(i - center_x) <= object.radius and  abs(j - center_y) <= object.radius):
                    grid_map[j][i] = 1
    
    return grid_map

def make_coefficient_array (grid_map, length, width, i , j):
    correction = 0
    counter = 0
    coefficient_array = standart_coefficient_array
    
    if (i + 1 < length + 2 and grid_map[i + 1][j] == 1):
        correction += coefficient_array[0][1]
        coefficient_array[0][1] = 0
        counter += 1
    
    if (i + 1 < length + 2 and j + 1 < width + 2 and grid_map[i + 1][j + 1] == 1):
        correction += coefficient_array[0][2]
        coefficient_array[0][2] = 0
        counter += 1
    
    if (j + 1 < width + 2 and grid_map[i][j + 1] == 1):
        correction += coefficient_array[1][2]
        coefficient_array[1][2] = 0
        counter += 1

    if (i - 1 >= 0 and j + 1 < width + 2 and grid_map[i - 1][j + 1] == 1):
        correction += coefficient_array[2][2]
        coefficient_array[2][2] = 0
        counter += 1

    if (i - 1 >= 0 and grid_map[i - 1][j] == 1):
        correction += coefficient_array[2][1]
        coefficient_array[2][1] = 0
        counter += 1

    if (i - 1 >= 0 and j - 1 >= 0 and grid_map[i - 1][j - 1] == 1):
        correction += coefficient_array[2][0]
        coefficient_array[2][0] = 0
        counter += 1

    if (j - 1 >= 0 and grid_map[i][j - 1] == 1):
        correction += coefficient_array[1][0]
        coefficient_array[1][0] = 0    
        counter += 1

    if (i + 1 < length + 2 and j - 1 >= 0 and grid_map[i + 1][j - 1] == 1):
        correction += coefficient_array[0][0]
        coefficient_array[0][0] = 0
        counter += 1

    coefficient_array *= correction / (9 - counter)
