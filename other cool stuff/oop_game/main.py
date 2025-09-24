import pygame 
from spritesheets import Spritesheet
import os
from fighter import Player
pygame.init()

SCREEN_W = 1920
SCREEN_H = int(SCREEN_W * 0.6)
player = Player(0.2)

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Valhalla Fighters")
# sheet = Spritesheet(os.path.join("assets/Puny-Characters", "Human-Soldier-Red.png"), 32, 32,4,5,0)
# sprites = sheet.get_all_sprites()
index = 0


# cols = sheet.get_cols()
# rows = sheet.get_rows()
index = 0
animation_speed = 0.2

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    # sprite = sprites[int(index) % len(sprites)]
    # screen.blit(sprite, (200,200))
    player.update(userInput)
    # index += animation_speed
    
    pygame.display.flip()
    clock.tick(60)
    userInput = pygame.key.get_pressed()

pygame.quit()
