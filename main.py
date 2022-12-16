import pygame
from draw import draw
import tkinter
from tkinter.filedialog import *
import sys
from color import *
from Object import *
# размеры экрана
WIDTH = 1260
HEIGHT = 700

colored_arr = [0] * 120  # дефолтный раскрашенный массив
for i in range(120):
    colored_arr[i] = [0] * 240
for i in range(120):
    for j in range(240):
        colored_arr[i][j] = [0] * 3

# цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (144, 238, 144)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
SKY = (210, 255, 255)
BLUE2 = (50, 225, 255)

# параметры кнопок главного меню 0
#x01 = 1060
#y01 = 10
#l01 = 120
#h01 = 25


"""class Button:  # класс кнопки
    def __init__(self, screen: pygame.Surface, color=GREY, x=0, y=0, w=0, h=0, text="", move=0):  # конструктор
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.move = move

    def draw(self):  # отрисовка
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
        font = pygame.font.Font(None, 20)
        text = font.render(self.text, True, BLACK)
        self.screen.blit(text, [self.x + 5, self.y + 8])"""


def menu_0(screen):
    #b1 = Button(screen, GREY, x01, y01, l01, h01, "Добавить объект")
    #buttons = [b1]
    #for b in buttons:
        #b.draw()
    for i in range(120):
        for j in range(240):
            pygame.draw.rect(screen, (colored_arr[i][j][0], colored_arr[i][j][1], colored_arr[i][j][2]),
                             pygame.Rect(j * 5 + 15, i * 5 + 60, 5, 5))
    pygame.display.update()  # обновление экрана

"""def mouse0(event): #отработка кнопок меню 0
    global objects
    global colored_arr
    if event.pos[0] >= x01 and event.pos[0] <=x01+l01 and event.pos[1] >= y01 and event.pos[1] <= y01+h01:
        converting("string_formula")
        colored_arr = coloring(calculating(objects))
    else:
        return 0"""

def main():
    black_screen_x = (15, 1215)
    black_screen_y = (60, 660)
    #создать объект массива объектов
    object_array = All_objects(black_screen_x[1] - black_screen_x[0], black_screen_y[1] - black_screen_y[0])
    global colored_arr
    #screen = pygame.display.set_mode((640, 480))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # экран
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(15, 10, 500, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    moving_object = False
    is_scalar_field = True
    screen.fill(WHITE)
    start_position = (0, 0)


    while not done:
        for event in pygame.event.get():
            menu_0(screen)
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                elif(event.pos[0] >= black_screen_x[0] and event.pos[0] <= black_screen_x[1] and event.pos[1] >= black_screen_y[0] and event.pos[1] <= black_screen_y[1]):
                    start_position = event.pos
                    moving_object = True
                    active = False
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.MOUSEBUTTONUP:
                if (moving_object):
                    object_array.move_object(start_position[0], start_position[1], event.pos[0], event.pos[1])
                    moving_object = False
                    draw(object_array.make_scalar_field(), is_scalar_field, screen, black_screen_x, black_screen_y)
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        object_array.add_object(text, int((black_screen_x[1] - black_screen_x[0]) / 2), int((black_screen_y[1] - black_screen_y[0]) / 2)) #добавили объект
                        draw(object_array.make_scalar_field(), is_scalar_field, screen, black_screen_x, black_screen_y)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif (event.key == pygame.K_SPACE):
                        is_scalar_field = not is_scalar_field
                        draw(object_array.make_scalar_field(), is_scalar_field, screen, black_screen_x, black_screen_y)
                    else:
                        text += event.unicode

        pygame.draw.rect(screen, WHITE, pygame.Rect(15, 10, 500, 32))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(1200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
