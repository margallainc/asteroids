import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # pygame is initialized
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # instantiate player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # FPS
    clock_object = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (asteroidfield, updatable)
    asteroid_field = AsteroidField()

    # Game loop starts here
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock_object.tick(60) / 1000


if __name__ == "__main__":
    main()
