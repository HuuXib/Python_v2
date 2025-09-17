import pygame
import random
from classes import Warrior , Background

pygame.init()

#Screen resolution

screen_h = 1080
screen_w = 1920
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Warrior Game")

def main():
    clock = pygame.time.Clock()
    player = Warrior()
    run = True  
    background = Background(screen_w, screen_h)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        background.update(player.run_velocity)
        userInput = pygame.key.get_pressed()
        background.draw(screen)

        player.update(userInput)
        screen.blit(player.image, (player.warrior_rect.x, player.warrior_rect.y))
        

        clock.tick(30)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()



