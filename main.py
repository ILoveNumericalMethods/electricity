import pygame
from draw import draw
from object import Object
from project import Project


def main():
    project = Project(1260, 700, (15, 1215), (60, 660))
    clock = pygame.time.Clock()

    done = False


    while not done:
        
        for event in pygame.event.get():
            
            done = project.handle_event(event)
            
        project.render_text()
            
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()