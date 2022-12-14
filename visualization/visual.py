import pygame
import tkinter
from tkinter.filedialog import *
import sys
from color import *

#размеры экрана
WIDTH = 1200
HEIGHT = 700

colored_arr = [] #массив с раскрашенными массивами
key = 0 #ключ есть ли что визуализировать

#цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (144, 238, 144)
MAGENTA = (255, 0, 255 )
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
SKY = (210, 255, 255)
BLUE2 = (50, 225, 255)

pygame.init() # начало работы с pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # экран
finished = False # программа не закончена
flag = 0
# Модуль pygame.image позволяет загрузить изображерие из файла и возвращает объект типа Surface.
#pygame.image.load("blue-rectangle-clip-art_233016-2769739325.png" )
# загрузить новое изображение из файла
#load(filename) -> Surface
# Загрузить изображение (путь к файлу для Windows)
#myImage = pygame.image.load('blue-rectangle-clip-art_233016-2769739325.png')
# определить место размещения
#myRect = (0,0,100,66)

#параметры кнопок главного меню 0
x01 = 375
y01 = 50
l01 = 300
h01 = 50

x02 = 400
y02 = 250
l02 = 400
h02 = 50

x03 = 400
y03 = 350
l03 = 400
h03 = 50

#параметры кнопок меню 1
x11 = 400
y11 = 50
l11 = 300
h11 = 50

x12 = 70
y12 = 150
l12 = 370
h12 = 50

x13 = 70
y13 = 250
l13 = 370
h13 = 50

x14 = 70
y14 = 350
l14 = 370
h14 = 50

x15 = 1000
y15 = 600
l15 = 150
h15 = 50

#параметры кнопок меню 2
x21 = 400
y21 = 50
l21 = 300
h21 = 50

x22 = 1000
y22 = 600
l22 = 150
h22 = 50

x23 = 100
y23 = 600
l23 = 300
h23 = 50

class Button: #класс кнопки
    def __init__(self, screen: pygame.Surface, color = GREY, x=0, y=0, w=0, h=0, text = "", move = 0): #конструктор
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.move = move
    def draw (self): #отрисовка
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
        font = pygame.font.Font(None, 50)
        text = font.render(self.text, True, BLACK)
        screen.blit(text, [self.x+5, self.y+8])

def open_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров из данного файла.
    Считанный массив, количество кадров и размеры - вывод функции
    """
    global key
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    key = 1
    return colored_array_from_file(in_filename)

def mouse0(event): #отработка кнопок меню 0
    if event.pos[0] >= x02 and event.pos[0] <=x02+l02 and event.pos[1] >= y02 and event.pos[1] <= y02+h02:
        return 1
    if event.pos[0] >= x03 and event.pos[0] <=x03+l03 and event.pos[1] >= y03 and event.pos[1] <= y03+h03:
        return 2
    else:
        return 0

def mouse1(event): #отработка кнопок меню 1
    if event.pos[0] >= x15 and event.pos[0] <=x15+l15 and event.pos[1] >= y15 and event.pos[1] <= y15+l15:
        return 0
    else:
        return 1

def mouse2(event): #отработка кнопок меню 2
    global colored_arr
    global k
    global m
    global n
    if event.pos[0] >= x22 and event.pos[0] <=x22+l22 and event.pos[1] >= y22 and event.pos[1] <= y22+h22:
        return 0
    if event.pos[0] >= x23 and event.pos[0] <=x23+l23 and event.pos[1] >= y23 and event.pos[1] <= y23+h23:
        colored_arr, k, m, n = open_file_dialog()
        return 2
    else:
        return 2

def menu1():
    b1 = Button(screen, SKY, x11, y11, l11, h11, "Рассчитать модель")
    b2 = Button(screen, BLUE2, x12, y12, l12, h12, "Разрешение экрана")
    b3 = Button(screen, BLUE2, x13, y13, l13, h13, "Объект")
    b4 = Button(screen, BLUE2, x14, y14, l14, h14, "Время визуализации")
    b5 = Button(screen, BLUE2, x15, y15, l15, h15, "Назад")
    buttons = [b1, b2, b3, b4, b5]
    for b in buttons:
        b.draw()

def menu2():
    global colored_arr
    global key
    global k
    global m
    global n
    b1 = Button(screen, SKY, x21, y21, l21, h21, "Визуализация файла")
    b2 = Button(screen, BLUE2, x22, y22, l22, h22, "Назад")
    b3 = Button(screen, BLUE2, x23, y23, l23, h23, "Выбрать файл")
    buttons = [b1, b2, b3]
    for b in buttons:
        b.draw()
    if key == 1:
        for t in range (k):
            for i in range (n):
                for j in range (m):
                    pygame.draw.rect(screen, (colored_arr[t][i][j][0], colored_arr[t][i][j][1], colored_arr[t][i][j][2]), pygame.Rect(j+100, i+120, 1, 1))
            pygame.display.update()  # обновление экрана
            pygame.time.delay(100) #задержка между кадрами


def menu0():
    b1 = Button(screen, SKY, x01, y01, l01, h01, "Визуализация потока воды")
    b2 = Button(screen, BLUE2, x02, y02, l02, h02, "Рассчитать модель")
    b3 = Button(screen, BLUE2, x03, y03, l03, h03, "Визуализация файла")
    buttons = [b1, b2, b3]
    for b in buttons:
        b.draw()
while not finished:
    screen.fill(SKY)
    if flag==0:
        menu0()
    if flag==1:
        menu1()
    if flag==2:
        menu2()
    for event in pygame.event.get(): # считываем события
        if event.type == pygame.QUIT: # завершение программы
            sys.exit()
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN: # нажатие мыши
            if flag == 0:
                flag = mouse0(event)
            elif flag == 1:
                flag = mouse1(event)
            elif flag == 2:
                flag = mouse2(event)
    pygame.display.update() # обновление экрана
pygame.quit()