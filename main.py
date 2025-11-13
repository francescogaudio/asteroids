import pygame
from pygame.locals import *
import sys
from constants import * 
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot
from player import *
from logger import log_state
from logger import log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    player = Player(x, y)
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0), )
        for drawables in drawable:
            drawables.draw(screen)
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


        pygame.display.flip()
        
        
        
if __name__ == "__main__":
    main()
