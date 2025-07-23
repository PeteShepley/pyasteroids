import sys
from constants import *
import pygame

from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # update
        updatable.update(dt)
            
        # render
        screen.fill(pygame.Color(0, 0, 0))
        
        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit(1)
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.kill()
                    shot.kill()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
