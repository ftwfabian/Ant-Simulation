from pygame.math import Vector2
import pygame

class AntHome:
    def __init__(self, position, screen):
        self.position = Vector2(position)
        self.screen = screen
    
    def draw(self):
        pygame.draw.circle(self.screen, (255,0,0), self.position, 10)