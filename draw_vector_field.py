import numpy
from math import atan
from math import cos
from math import sin
import pygame

def draw_circle (screen, x, y, x_vector, y_vector, max_length):
    angle = atan(y_vector / x_vector)
    new_vector_length = ((x_vector ** 2 + y_vector ** 2) ** 0,5 / max_length) * 10

    rotate_matrix = numpy.array([[cos(angle), sin(angle)],
                               [-1 * sin(angle), cos(angle)]])
    center_point = numpy.array([[x + 1],
                               [y]]) 
    up_point = numpy.array([[x + 1 - (1 / 3)],
                               [y - (1 / 3)]])
    down_point = numpy.array([[x + 1 - (1 / 3)],
                               [y + (1 / 3)]])
    center_point = center_point*new_vector_length
    up_point = up_point*new_vector_length
    down_point = down_point*new_vector_length

    center_point = numpy.dot(rotate_matrix, center_point)
    up_point = numpy.dot(rotate_matrix, up_point)
    down_point = numpy.dot(rotate_matrix, down_point)


    pygame.draw.polygon(screen, (225, 225, 0), ((x, y), (center_point[0][0], center_point[1][0]), (up_point[0][0], up_point[1][0]), (center_point[0][0], center_point[1][0]), (down_point[0][0], down_point[1][0])))

def draw_vector_field (scalar_field, screen, screen_x, screen_y):
    distance_between_vectors = 10
    
    for y in range(screen_y[1] - screen_y[0]):
        for x in range(screen_x[1] - screen_x[0]):
            if (scalar_field[y][x] == -1):
                pygame.draw.rect(screen, (0, 0, 139), (x, y, 1, 1))

    max_length = 0
    for y in range(1, screen_y[1] - screen_y[0], distance_between_vectors):
        for x in range(1, screen_x[1] - screen_x[0], distance_between_vectors): 
            if (scalar_field[y][x] == -1):
                continue
           
            x_vector = scalar_field[y][x + 1] - scalar_field[y][x]
            y_vector = scalar_field[y + 1][x] - scalar_field[y][x]
            max_length = max(max_length, (x_vector ** 2 + y_vector ** 2) ** 0,5)
    
    for y in range(1, screen_y[1] - screen_y[0], distance_between_vectors):
        for x in range(1, screen_x[1] - screen_x[0], distance_between_vectors):
            if (scalar_field[y][x] == -1):
                continue

            x_vector = scalar_field[y][x + 1] - scalar_field[y][x]
            y_vector = scalar_field[y + 1][x] - scalar_field[y][x]

            draw_circle(screen, x + screen_x[0], y + screen_y[0], x_vector, y_vector, max_length)