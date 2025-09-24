import pygame 
import os 
from spritesheets import Spritesheet
SCREEN_W = 1920
SCREEN_H = int(SCREEN_W * 0.6)
# SHEET = Spritesheet(os.path.join("assets/Puny-Characters", "Human-Soldier-Red.png"), 32, 32,4)



class Player():
    #Start coordinates (middle of the screen)
    x_position = SCREEN_W // 2
    y_position = SCREEN_H // 2
    move_velocity = 10

    def __init__(self,animation_speed):
        self.animation_speed = animation_speed
        #assets
        #Sheet init
        self.sprites = Spritesheet(os.path.join("assets/Puny-Characters", "Human-Soldier-Red.png"), 32, 32,4).get_all_sprites()
        #animation step index 
        self.index = 0
        self.step_index = 0
        #particular animations 
        self.animations = {
            'moveup': self.sprites[95:111],
            'moveback': self.sprites[0:6],
            'moveleft': self.sprites[143:149],
            'moveright': self.sprites[71:77],
            'attack': self.sprites[6:10], 
            'idle': self.sprites[17:19], 
        }
        
        #state init
        self.player_move_up = False
        self.player_attack = False
        self.player_idle = False

        #hitbox init
        # self.hitbox_image = self.player_move_up[0]
        # self.hitbox = self.hitbox_image.get_rect()

        #hitbox coordinates
        # self.hitbox.x = self.x_position
        # self.hitbox.y = self.y_position

    def update(self, userInput):

        if (userInput[pygame.K_w]):
            self.player_move_up = True
            self.player_attack = False
            self.player_idle = False
        if (userInput[pygame.K_f]):
            self.player_move_up = False
            self.player_attack = True
            self.player_idle = False
        else:
            self.player_move_up =  False
            self.player_attack = False
            self.player_idle = True

        if self.player_move_up:
            self.move_up()
        # if self.player_attack:
        #     self.attack()
        if self.player_idle:
            self.idle()


    def move_up(self):
        self.image = self.animations['moveup']
        self.y_position -= self.move_velocity
        self.step_index += self.animation_speed
        if self.step_index >= len(self.image):
            self.step_index = 0
    # def attack(self):
    #     self.image = self.attack_img[self.step_index % len(self.attack_img)]
    #     self.x_position += self.move_velocity
    #     self.step_index += 1
    #     if self.step_index >= len(self.attack_img):
    #         self.step_index = 0
    def idle(self):
        self.image = self.animations['idle']
        self.x_position += self.move_velocity
        self.step_index += 1
        if self.step_index >= len(self.image):
            self.step_index = 0   
    