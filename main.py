# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    pygame.init()


    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable) 

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))

        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                raise SystemExit("Game Over")
        for asteroid in asteroids:
            for shot in shots: 
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.kill()
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

