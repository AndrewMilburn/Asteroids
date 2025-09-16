import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game Over")
                sys.exit()



# drawable.draw(screen) - Can't do this as there is no associated Image for the SPRITE
# which is what the underlying class is derived from 
        for stuff in drawable:
            stuff.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000
    #    print(f"FPS:{1/dt}")

if __name__ == "__main__":
    main()
