from Ant import Ant
from AntHome import AntHome
from Container import Container
from Food import Food
import pygame
import random
from pygame.math import Vector2

if __name__ == '__main__':
    pygame.init()
    container_length = 1000
    container_height = 500
    screen = pygame.display.set_mode((container_length,container_height))
    container = Container(container_length, container_height)
    pygame.display.set_caption('Ants')
    clock = pygame.time.Clock()
    
    running = True
    
    ant_list = []
    ant_home_list = []
    food_list = []

    for i in range(0,2):
        ant_home_list.append(AntHome([random.randint(20,container_length-20), random.randint(20, container_height-20)], screen))
    for i in range(0,2):
        food_list.append(Food([random.randint(50,container_length-50),random.randint(50,container_height-50)], screen))
    for i in range(0,10):
        for home in ant_home_list:
            ant_list.append(Ant(home.position, [random.randint(-100,100), random.randint(-100,100)], screen, container))
    container.set_agents(ant_list,food_list, ant_home_list)

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255,255,255))
        container.run_all()
        container.draw_all()
        pygame.display.flip()
        clock.tick(200)


pygame.quit()