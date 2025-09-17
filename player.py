import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        tringle = self.triangle()
        pygame.draw.polygon(screen, pygame.Color('white'), tringle, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_o]:
            self.rotate(-dt)
        if keys[pygame.K_i]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.move(-dt)
        if keys[pygame.K_RETURN]:
            self.shoot()
        self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_VELOCITY * dt

    def shoot(self):
        if self.timer < 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOT_COOLDOWN


        
