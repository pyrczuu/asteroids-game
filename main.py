import sys
import pygame

from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0                  # delta time (time diff)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable, drawable)

    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (drawable, updatable, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    print("HIT")
                    pygame.sprite.Sprite.kill(asteroid)
                    pygame.sprite.Sprite.kill(shot)
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
