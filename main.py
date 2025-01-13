import pygame
from constants import *
from player import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    framerate = 60

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(framerate) / 1000

if __name__ == "__main__":
    main()