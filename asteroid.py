import pygame
from circleshape import CircleShape
#from random import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, xpos, ypos, radius):
        super().__init__(xpos, ypos, radius)

    def draw(self, screen):
       pygame.draw.circle(screen, pygame.Color('white'), self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            offsplit_1 = Asteroid(self.position.x, self.position.y, self.radius)
            offsplit_1.velocity += self.velocity.rotate(angle)
            offsplit_1.radius -= ASTEROID_MIN_RADIUS
            offsplit_1.velocity *= 1.2
            offsplit_2 = Asteroid(self.position.x, self.position.y, self.radius)
            offsplit_2.velocity -= self.velocity.rotate(angle)
            offsplit_2.radius -= ASTEROID_MIN_RADIUS
            offsplit_2.velocity *= 1.2

