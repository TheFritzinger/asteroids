import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        for asteroid in asteroids:
            if player.checkCollisions(asteroid) == True:
                print("Game over!")
                return 1


        screen.fill(000000)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000
   

if __name__ == "__main__":
    main()
