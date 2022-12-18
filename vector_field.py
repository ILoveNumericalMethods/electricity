import pygame

def draw_vector_field (scalar_field, screen, screen_x, screen_y):
   """
   GREED_STEP = distace between vectors
   """
   GREED_STEP = 20
   YELLOW = (255, 255, 0)

   for y in range(1, screen_y[1] - screen_y[0], GREED_STEP):
        for x in range(1, screen_x[1] - screen_x[0], GREED_STEP):
            vector_x = scalar_field[y][x + 1] - scalar_field[y][x]
            vector_y = scalar_field[y + 1][x] - scalar_field[y][x]

            pygame.draw.aaline(screen, YELLOW, (x, y), (x + vector_x, y + vector_y))
