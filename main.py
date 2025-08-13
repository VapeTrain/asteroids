import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    delta_time = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updateable
    Asteroid.containers = (asteroids, updateable, drawable)
    asteroid_field = AsteroidField()
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    
    dt = 0
    ship = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            if a.collision_check(ship):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if a.collision_check(shot):
                    shot.kill()
                    a.split()

        pygame.display.flip()

        dt = delta_time.tick(60) / 1000

if __name__ == "__main__":
    main()
