import pygame
import sys
from pygame import mixer
from classes import Warrior, Background, Camera, Enemy  

pygame.init()
mixer.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Warrior Game")



warrior = Warrior(SCREEN_WIDTH, SCREEN_HEIGHT)
background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, warrior.world_width, warrior.world_height)
enemy = Enemy()




clock = pygame.time.Clock()
running = True

# Główna pętla gry
# Główna pętla gry
# Główna pętla gry
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False



    # Inne aktualizacje gry
    userInput = pygame.key.get_pressed()
    warrior.update(userInput)
    enemy.update()
    screen.blit(enemy.image, (Warrior.X_POS, Warrior.Y_POS))
    camera.follow(warrior.warrior_rect.centerx, warrior.warrior_rect.centery)
    background.update(warrior.run_velocity, camera.x)
    background.draw(screen)
    screen.blit(warrior.image, camera.apply(warrior.warrior_rect.x, warrior.warrior_rect.y))

    pygame.display.update()
    clock.tick(30)


pygame.quit()
sys.exit()