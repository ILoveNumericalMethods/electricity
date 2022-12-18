import pygame
from cocos_draw import cocos_draw
from draw import draw
from object import All_objects
import pygame


WHITE = (255, 255, 255)

class Input_area:
    """
    input box class
    geometry - coordinates - object of class Rect
    is_active - whether input is active
    text - text string
    colour - colour
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
    program class
    WIDTH - screen width
    HEIGHT - screen height
    black_screen_x - x coordinate of the left and right edges of the black screen
    black_screen_y - y-coordinate of top and bottom edges of black screen
    is_scalar_field - whether the scalar field is rendered
    moving_object - whether an object is moving
    screen - screen
    input_area - input area
    start_position - point from where the object moves
    """

    def __init__ (self, WIDTH, HEIGHT, black_screen_x, black_screen_y):

        self.black_screen_x = black_screen_x
        self.black_screen_y = black_screen_y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.is_scalar_field = True
        self.moving_object = False
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.object_array =  All_objects(self.black_screen_y[1] - self.black_screen_y[0], self.black_screen_x[1] - self.black_screen_x[0])
        self.input_area = Input_area(15, 10, 500, 32)
        self.font = pygame.font.Font(None, 32)
        self.start_position = (0, 0)

        self.screen.fill(WHITE)

    def handle_event(self, event):

        if event.type == pygame.QUIT:
            return True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button == 1):
                if self.input_area.geometry.collidepoint(event.pos):
                    self.input_area.is_active = True

                elif(event.pos[0] >= self.black_screen_x[0] and event.pos[0] <= self.black_screen_x[1] and event.pos[1] >= self.black_screen_y[0] and event.pos[1] <= self.black_screen_y[1]):
                    if (self.object_array.find_best_object(event.pos[0], event.pos[1]) != -1):
                        self.start_position = event.pos
                        self.moving_object = True
                    
                    self.input_area.is_active = False

                else:
                    self.input_area.is_active = False

                self.input_area.change_color()
            
            elif(event.pos[0] >= self.black_screen_x[0] and event.pos[0] <= self.black_screen_x[1] and event.pos[1] >= self.black_screen_y[0] and event.pos[1] <= self.black_screen_y[1]):
                if (self.object_array.find_best_object(event.pos[0], event.pos[1]) != -1):
                    self.object_array.delete_object(event.pos[0], event.pos[1])
                    cocos_draw(self.object_array.make_scalar_field()[0], self.object_array.make_scalar_field()[1], self.screen, self.black_screen_x, self.black_screen_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.moving_object:
                self.object_array.move_object(self.start_position[0], self.start_position[1], event.pos[0], event.pos[1])
                
                self.moving_object = False
                cocos_draw(self.object_array.make_scalar_field()[0], self.object_array.make_scalar_field()[1], self.screen, self.black_screen_x, self.black_screen_y)

        elif event.type == pygame.KEYDOWN:
            if self.input_area.is_active:
                
                if event.unicode == '\r': #this is terrible but for some reason (Anton Rudenko) i will do it
                    self.object_array.add_object(self.input_area.text, int((self.black_screen_x[1] - self.black_screen_x[0]) / 2), int((self.black_screen_y[1] - self.black_screen_y[0]) / 2))
                    cocos_draw(self.object_array.make_scalar_field()[0], self.object_array.make_scalar_field()[1], self.screen, self.black_screen_x, self.black_screen_y)
                    self.input_area.text = ""
                
                elif event.key == pygame.K_BACKSPACE:
                    self.input_area.text = self.input_area.text[:-1]
                
                elif (event.key == pygame.K_SPACE and self.input_area.is_active != True):
                    self.is_scalar_field = not self.is_scalar_field
                    print (self.is_scalar_field)
                    cocos_draw(self.object_array.make_scalar_field()[0], self.object_array.make_scalar_field()[1], self.screen, self.black_screen_x, self.black_screen_y)

                else:
                    self.input_area.text += event.unicode

            elif (event.key == pygame.K_SPACE):
                self.is_scalar_field = not self.is_scalar_field
                print (self.is_scalar_field)
                cocos_draw(self.object_array.make_scalar_field()[0], self.object_array.make_scalar_field()[1], self.screen, self.black_screen_x, self.black_screen_y)
        
        return False


    def render_text(self):
        pygame.draw.rect(self.screen, WHITE, self.input_area.geometry)
        txt_surface = self.font.render(self.input_area.text, True, self.input_area.color)
        width = max(1200, txt_surface.get_width()+10)
        self.input_area.geometry.w = width
        self.screen.blit(txt_surface, (self.input_area.geometry.x + 5, self.input_area.geometry.y + 5))
        pygame.draw.rect(self.screen, self.input_area.color, self.input_area.geometry, 2)
