from pygame.math import Vector2
import pygame

class Food:
    def __init__(self, position, screen):
        self.position = Vector2(position)
        self.radius = 5
        self.screen = screen
    
    def draw(self):
        if self.radius > 0:
            pygame.draw.circle(self.screen, (0,255,0), self.position, self.radius)

    def decrement_food(self):
        self.radius = self.radius - 1
