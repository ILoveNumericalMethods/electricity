import pygame
from draw import draw
from object import All_objects
import pygame

WHITE = (255, 255, 255)

class Input_area:
    """
    ����� ���� �����
    geometry - ���������� - ������ ������ Rect
    is_active - ������� �� ����
    text - ����� ������
    color - ����
    """
    def __init__ (self, start_x, start_y, width, height):
        self.geometry = pygame.Rect(start_x, start_y, width, height)
        self.is_active = False
        self.text = ""
        self.color = pygame.Color('lightskyblue3')
    
    def change_color(self):
        if (self.is_active):
            self.color = pygame.Color('dodgerblue2')
        else:
            self.color = pygame.Color('lightskyblue3')

    

class Project:
    """
    ����� ���������
    WIDTH - ������ ������
    HEIGHT - ������ ������
    black_screen_x - ���������� x ������ � ������� ���� ������� ������
    black_screen_y - ���������� y �������� � ������� ���� ������� ������
    is_scalar_field - ��������������� �� ��������� ����
    moving_object - ��������� �� ������
    screen - �����
    input_area - ������� ����� 
    start_position - ����� ������ �������� ������
    """

    def __init__ (self, WIDTH, HEIGHT, black_screen_x, black_screen_y):

        self.black_screen_x = black_screen_x
        self.black_screen_y = black_screen_y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.is_scalar_field = True
        self.moving_oject = False
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.object_array =  All_objects(self.black_screen_x[1] - self.black_screen_x[0], self.black_screen_y[1] - self.black_screen_y[0])
        self.input_area = Input_area(15, 10, 500, 32)
        self.start_position = (0, 0)

        screen.fill(WHITE)

    def handle_event(self, event):

        if event.type == pygame.QUIT:
            return True

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.input_area.geometry.collidepoint(event.pos):
                self.input_area.is_active = True
            elif(event.pos[0] >= self.black_screen_x[0] and event.pos[0] <= self.black_screen_x[1] and event.pos[1] >= self.black_screen_y[0] and event.pos[1] <= self.black_screen_y[1]):
                self.start_position = event.pos
                self.moving_object = True
                self.input_area.is_active = False
            else:
                self.input_area.is_active = False
            self.input_area.change_color()
        
        if event.type == pygame.MOUSEBUTTONUP:
            if self.moving_object:
                self.object_array.move_object(self.start_position[0], self.start_position[1], event.pos[0], event.pos[1])
                
                self.moving_object = False
                draw(self.object_array.make_scalar_field(), self.is_scalar_field, self.screen, self.black_screen_x, self.black_screen_y)
        
        if event.type == pygame.KEYDOWN:
            if self.input_area.is_active:
                
                if event.key == pygame.K_RETURN:
                    
                    self.object_array.add_object(self.input_area.text, int((self.black_screen_x[1] - self.black_screen_x[0]) / 2), int((self.black_screen_y[1] - self.black_screen_y[0]) / 2))
                    draw(self.object_array.make_scalar_field(), self.is_scalar_field, self.screen, self.black_screen_x, self.black_screen_y)
                    self.input_area.text = ""
                
                elif event.key == pygame.K_BACKSPACE:
                    self.input_area.text = self.input_area.text[:-1]
                elif (event.key == pygame.K_SPACE):
                    self.is_scalar_field = not self.is_scalar_field
                    draw(self.object_array.make_scalar_field(), self.is_scalar_field, self.screen, self.black_screen_x, self.black_screen_y)
                else:
                    self.input_area.text += event.unicode
        return False


    def render_text(self):
        pygame.draw.rect(self.screen, WHITE, self.input_area.geometry)
        txt_surface = font.render(text, True, color)
        width = max(1200, txt_surface.get_width()+10)
        self.input_area.geometry.w = width
        screen.blit(txt_surface, (self.input_area.geometry.x + 5, self.input_area.geometry.y + 5))
        pygame.draw.rect(self.screen, self.input_area.color, self.input_area.geometry, 2)
