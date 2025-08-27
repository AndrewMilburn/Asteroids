import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))


        updatable.update(dt)
# drawable.draw(screen) - Can't do this as there is no associated Image for the SPRITE
# which is what the underlying class is derived from 
        for stuff in drawable:
            stuff.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000
    #    print(f"FPS:{1/dt}")

if __name__ == "__main__":
    main()
