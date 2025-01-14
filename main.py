import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    framerate = 60
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.check_collision(player):
                raise SystemExit("Game over!")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(framerate) / 1000

if __name__ == "__main__":
    main()