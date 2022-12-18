from draw_vector_field import draw_vector_field
import pygame
def cocos_draw(scalar_field, max_potential, screen, screen_x, screen_y):
    
    if(max_potential == 0):
        max_potential = 1

    r = 255 / max_potential
    g = -86 / max_potential
    b = -145 / max_potential

    for y in range(screen_y[1] - screen_y[0]):
        for x in range(screen_x[1] - screen_x[0]):
            
            if(scalar_field[y][x] == -1):
                pygame.draw.rect(screen, (160, 82, 45), pygame.Rect(x + screen_x[0], y + screen_y[0], 1, 1))

            else:
                pygame.draw.rect(screen, (int(r * scalar_field[y][x]), int(g * scalar_field[y][x] + 191), int(225 + b * scalar_field[y][x])),
                                pygame.Rect(x + screen_x[0], y + screen_y[0], 1, 1))
    pygame.display.update()  