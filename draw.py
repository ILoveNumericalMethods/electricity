from color import coloring
from draw_vector_field import draw_vector_field
import pygame

def draw (scalar_field, is_scalar_filed, screen, screen_x, screen_y):
    if (is_scalar_filed):
            colored_arr = coloring(scalar_field)
            for y in range(screen_y[1] - screen_y[0] - 1):
                for x in range(screen_x[1] - screen_x[0] - 1):
                    pygame.draw.rect(screen, (colored_arr[y][x][0], colored_arr[y][x][1], colored_arr[y][x][2]),
                                     pygame.Rect(x + screen_x[0], y + screen_y[0], 1, 1))
            pygame.display.update()  
    else:
        draw_vector_field(scalar_field, screen, screen_x, screen_y)
        pygame.display.update()
