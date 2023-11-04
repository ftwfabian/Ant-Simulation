from pygame.math import Vector2
import math
import pygame
#from VectorMath import positions_are_very_near

class Ant:
    def __init__(self, position, direction,screen,container):
        self.position = Vector2(position)
        self.direction = Vector2(direction).normalize()
        self.sight_distance = 20
        self.sight_angle = math.radians(90)
        self.carrying_food = False
        self.sees_food = False
        self.speed = 1
        self.screen = screen
        self.container = container

    def move(self):
        if self.position[0] <= 0+5 or self.position[0] >= self.container.length - 5:
            self.direction[0] = -1 * self.direction[0]
        if self.position[1] <= 0+5 or self.position[1] >= self.container.height - 5:
            self.direction[1] = -1 * self.direction[1]
        self.position = self.position + self.direction
        print(self.position)
        print(type(self.position))

    def draw(self):
        pygame.draw.circle(self.screen, (0,0,0), self.position, 2)









    
