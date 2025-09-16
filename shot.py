import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, xpos, ypos, radius):
        super().__init__(xpos, ypos, radius)

    def draw(self, screen):
       pygame.draw.circle(screen, pygame.Color('white'), self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt
