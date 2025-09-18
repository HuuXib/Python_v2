import pygame
import os
from pygame import mixer
import time
import random

mixer.init()
MOVING = [pygame.image.load(os.path.join("assets/move","t1.png" )),
          pygame.image.load(os.path.join("assets/move","t3.png" )),
          pygame.image.load(os.path.join("assets/move","t4.png" )),
          pygame.image.load(os.path.join("assets/move","t5.png" )),
          pygame.image.load(os.path.join("assets/move","t6.png" )),
          pygame.image.load(os.path.join("assets/move","t7.png" )),
          pygame.image.load(os.path.join("assets/move","t8.png" )),
          pygame.image.load(os.path.join("assets/move","t9.png" )),
          pygame.image.load(os.path.join("assets/move","t10.png" ))]
IDLE = [pygame.image.load(os.path.join("assets/idle","i1.png" )),
        pygame.image.load(os.path.join("assets/idle","i2.png" ))]

RUNNING = [pygame.image.load(os.path.join("assets/run","k1.png" )),
           pygame.image.load(os.path.join("assets/run","k2.png" )),
           pygame.image.load(os.path.join("assets/run","k3.png" )),
           pygame.image.load(os.path.join("assets/run","k4.png" )),
           pygame.image.load(os.path.join("assets/run","k5.png" )),
           pygame.image.load(os.path.join("assets/run","k6.png" )),
           pygame.image.load(os.path.join("assets/run","k7.png" )),
           pygame.image.load(os.path.join("assets/run","k8.png" ))]

ATTACK = [pygame.image.load(os.path.join("assets/attack","a1.png" )),
          pygame.image.load(os.path.join("assets/attack","a2.png" )),
          pygame.image.load(os.path.join("assets/attack","a3.png" )),
          pygame.image.load(os.path.join("assets/attack","a4.png" )),
          pygame.image.load(os.path.join("assets/attack","a5.png" )),
          pygame.image.load(os.path.join("assets/attack","a6.png" )),
          pygame.image.load(os.path.join("assets/attack","a7.png" )),
          pygame.image.load(os.path.join("assets/attack","a8.png" )),
          pygame.image.load(os.path.join("assets/attack","a9.png" )),
          pygame.image.load(os.path.join("assets/attack","a10.png" )),
          pygame.image.load(os.path.join("assets/attack","a11.png" )),
          pygame.image.load(os.path.join("assets/attack","a12.png" )),
          pygame.image.load(os.path.join("assets/attack","a13.png" ))]


FOOTSTEP_NOISES = [pygame.mixer.Sound(os.path.join("assets/footsteps", "01-footstep.ogg")),
                   pygame.mixer.Sound(os.path.join("assets/footsteps", "02-footstep.ogg")),
                   pygame.mixer.Sound(os.path.join("assets/footsteps", "03-footstep.ogg")),
                   pygame.mixer.Sound(os.path.join("assets/footsteps", "04-footstep.ogg")),
                   pygame.mixer.Sound(os.path.join("assets/footsteps", "05-footstep.ogg")),
                   pygame.mixer.Sound(os.path.join("assets/footsteps", "06-footstep.ogg"))]


#Enemy assets 
BOF_IDLE = [pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Idle","Bringer-of-Death_Idle_1.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Idle","Bringer-of-Death_Idle_2.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Idle","Bringer-of-Death_Idle_3.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Idle","Bringer-of-Death_Idle_4.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Idle","Bringer-of-Death_Idle_5.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Idle","Bringer-of-Death_Idle_6.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Idle","Bringer-of-Death_Idle_7.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Idle","Bringer-of-Death_Idle_8.png" ))] 

BOF_ATTACK = [pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_1.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_2.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_3.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_4.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_5.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_6.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_7.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_8.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_9.png" )),
            pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Attack","Bringer-of-Death_Attack_10.png" ))] 

BOF_RUNNING = [pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Walk","Bringer-of-Death_Walk_1.png" )),
               pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Walk","Bringer-of-Death_Walk_2.png" )),
               pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Walk","Bringer-of-Death_Walk_3.png" )),
               pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Walk","Bringer-of-Death_Walk_4.png" )),
               pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Walk","Bringer-of-Death_Walk_5.png" )),
               pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Walk","Bringer-of-Death_Walk_6.png" )),
               pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Walk","Bringer-of-Death_Walk_7.png" )),
               pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Walk","Bringer-of-Death_Walk_8.png" ))]

BOF_DEATH = [pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_1.png" )),
             pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_2.png" )),
             pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_3.png" )),
             pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_4.png" )),
             pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_5.png" )),
             pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_6.png" )),
             pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_7.png" )),
             pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_8.png" )),
             pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_9.png" )),
             pygame.image.load(os.path.join("assets/Enemies/Bringer-Of-Death/Individual_Sprite/Death","Bringer-of-Death_Death_10.png" ))]





BACKGROUND_FOREST_BACK = pygame.image.load(os.path.join("assets/parallax_forest_pack/layers","parallax-forest-back-trees.png"))
BACKGROUND_FOREST_MID = pygame.image.load(os.path.join("assets/parallax_forest_pack/layers","parallax-forest-middle-trees.png"))
BACKGROUND_FOREST_FRONT = pygame.image.load(os.path.join("assets/parallax_forest_pack/layers","parallax-forest-front-trees.png"))
BACKGROUND_FOREST_LIGHT = pygame.image.load(os.path.join("assets/parallax_forest_pack/layers","parallax-forest-lights.png"))

game_speed = 10
SOUNDTRACK = pygame.mixer.Sound(os.path.join("assets/soundtrack", "GameMusic_ForestTheme_24.mp3"))
SOUNDTRACK.set_volume(0.1)
SOUNDTRACK.play(loops=-1)


class Warrior:
    X_POS = 80 
    Y_POS = 310
    step_index = 0
    
    RUN_VELOCITY = 0

    def __init__(self):
        self.footsteps_noises = FOOTSTEP_NOISES
        self.sword_sound = pygame.mixer.Sound(os.path.join("assets/melee_sounds", "sword sound.wav"))
        self.sword_sound.set_volume(0.7)
        self.sound_played = False
        self.step_index = 0
        self.move_img = MOVING
        self.run_img = RUNNING
        self.attack_img = ATTACK
        self.idle_img = IDLE
        self.Y_POS = 1080 - self.idle_img[0].get_height()
        self.sword_sound.set_volume(0.7)
        self.sound_played = False

        # self.move_img = [pygame.transform.scale(img, (1920, 1080)) for img in RUNNING]
        # self.run_img = [pygame.transform.scale(img, (1920, 1080)) for img in RUNNING]
        # self.attack_img = [pygame.transform.scale(img, (1920, 1080)) for img in ATTACK]
        # self.idle_img = [pygame.transform.scale(img, (1920, 1080)) for img in IDLE]


        self.run_img_left = [pygame.transform.flip(img, True, False) for img in self.run_img]

        self.warrior_move = False
        self.warrior_run = False
        self.warrior_attack = False
        self.warrior_idle = True
        self.warrior_run_back = False

        self.run_velocity = self.RUN_VELOCITY
        self.image = self.idle_img[0]
        self.warrior_rect = self.image.get_rect()
        self.warrior_rect.x = self.X_POS
        self.warrior_rect.y = self.Y_POS

        
    def update(self, userInput):

        if (userInput[pygame.K_a] or userInput[pygame.K_d]) and userInput[pygame.K_LSHIFT]:
            self.run_velocity = 30
            self.warrior_idle = False
            self.warrior_run = True
            self.warrior_attack = False
            self.warrior_move = False
        elif userInput[pygame.K_f]:
            self.warrior_idle = False
            self.warrior_run = False
            self.warrior_attack = True
            self.warrior_move = False  
        elif userInput[pygame.K_d]:
            self.warrior_idle = False
            self.warrior_run = False
            self.warrior_attack = False
            self.warrior_move = True
        elif userInput[pygame.K_a]:
            self.warrior_run_back = True
            self.warrior_idle = False
            self.warrior_run = False
            self.warrior_attack = False
            self.warrior_move = False
        else:
            self.warrior_idle = True
            self.warrior_run = False
            self.warrior_attack = False
            self.warrior_move = False
            self.warrior_run_back = False
        if self.warrior_move:
            self.run()
        if self.warrior_run_back:
            self.moveback()
        if self.warrior_run:
            self.run()
        if self.warrior_idle:
            self.idle()
        if self.warrior_attack:
            self.attack()
        if self.step_index >= 1000: 
            self.step_index = 0
    def run(self):
        if self.step_index == 0 or self.step_index%4 == 0:
            self.footsteps_noises[random.randint(0,5)].play()
        self.image = self.run_img[self.step_index % len(self.run_img)]
        self.run_velocity = 30
        self.warrior_rect.x += self.run_velocity
        self.step_index += 1
        if self.step_index >= len(self.run_img):
            self.step_index = 0
    def moveback(self):
        if self.step_index == 0 or self.step_index%4 == 0:
            self.footsteps_noises[random.randint(0,5)].play()
        self.run_velocity = -30
        self.image = self.run_img_left[self.step_index  % len(self.run_img_left)]
        self.warrior_rect.x += self.run_velocity
        self.step_index += 1
        if self.step_index >= len(self.run_img_left): 
            self.step_index = 0
    def idle(self):
        self.run_velocity = 0
        self.image = self.idle_img[self.step_index //8 % len(self.idle_img)]
        self.step_index += 1
        if self.step_index >= 8* len(self.idle_img): 
            self.step_index = 0
    def attack(self):
        if self.step_index == 0 or self.step_index == 6 or self.step_index == 11 and not self.sound_played :
            self.sword_sound.play()
            self.sound_played = True
        self.image = self.attack_img[self.step_index *2  % len(self.attack_img)]
        self.step_index += 1
        # if self.step_index >= 2* len(self.attack_img):
        #     self.step_index = 0
        if self.step_index >= len(self.attack_img) // 2:
            self.step_index = 0
            self.sound_played = False


class Background():
    

    def __init__(self, screen_width, screen_height):
        # self.zmienna_z_klasy_a = klasa_a.zmienna
        self.run_velocity = Warrior.RUN_VELOCITY
        self.back_trees = BACKGROUND_FOREST_BACK
        self.mid_trees = BACKGROUND_FOREST_MID
        self.front_trees = BACKGROUND_FOREST_FRONT
        self.light = BACKGROUND_FOREST_LIGHT

        self.back_trees = pygame.transform.scale(self.back_trees, (screen_width, screen_height))
        self.mid_trees = pygame.transform.scale(self.mid_trees, (screen_width, screen_height))
        self.front_trees = pygame.transform.scale(self.front_trees, (screen_width, screen_height))
        self.light = pygame.transform.scale(self.light, (screen_width, screen_height))

        self.back_x = 0
        self.mid_x = 0
        self.front_x = 0
        self.light_x = 0

        self.back_speed = 0.5
        self.mid_speed = 1.5
        self.front_speed = 3
        self.light_speed = 2
    def update(self, player_velocity):
        self.back_x -= self.back_speed * player_velocity
        self.mid_x -= self.mid_speed * player_velocity
        self.front_x -= self.front_speed * player_velocity
        self.light_x -= self.light_speed + player_velocity

        #zapetlanie obrazkow

        screen_width = self.back_trees.get_width()

        #ruch
        self.back_x %= screen_width
        self.mid_x %= screen_width
        self.front_x %= screen_width
        self.light_x %= screen_width

    def draw(self, screen):
        direction = 1 if self.run_velocity == 30 else -1
        screen.blit(self.back_trees, (self.back_x, 0))
        screen.blit(self.back_trees, (self.back_x + direction * self.back_trees.get_width(), 0))
        screen.blit(self.mid_trees, (self.mid_x, 0))
        screen.blit(self.mid_trees, (self.mid_x + direction *self.mid_trees.get_width(), 0))
        screen.blit(self.front_trees, (self.front_x, 0))
        screen.blit(self.front_trees, (self.front_x + direction *self.front_trees.get_width(), 0))
        screen.blit(self.light, (self.light_x, 0))
        screen.blit(self.light, (self.light_x + direction *self.light.get_width(), 0))


class Camera():
    def __init__(self, screen_width, screen_height ,world_width, world_height):
        self.x = 0
        self.y = 0
        self.screen_width = screen_width
        self.screen_height= screen_height
        self.world_width = world_width
        self.world_height = world_height
        self.smoothness = 0.1

    def follow(self, target_x, target_y):
        target_camera_x = target_x - self.screen_width //2
        target_camera_y = target_y = self.screen_height //2


        self.x += (target_camera_x - self.x) *self.smoothness
        self.y += (target_camera_y - self.y) * self.smoothness

        self.x = max(0, min(self.x, self.world_width - self.screen_height))

    def apply(self, x , y):
        return x - self.x, y- self.y
    
    def get_viev_rect(self):
        return pygame.Rect(self.x, self.y, self.screen_width, self.screen_height)
    




class Enemy():
    step_index = 0
    RUN_VELOCITY = 0
    health = 100
    def __init__(self):
        self.run_img = BOF_RUNNING
        self.idle_img = BOF_IDLE
        self.attack_img = BOF_ATTACK
        self.death_img = BOF_DEATH
        self.Player = Warrior()
        self.Player_rect = self.Player.warrior_rect
        self.Player_X_POS = Warrior.X_POS
        self.Player_Y_POS = Warrior.Y_POS
        self.X_POS = self.Player_X_POS + random.randint(-1000,1000)
        self.Y_POS = 1080 - self.idle_img[0].get_height()
        self.enemy_hitbox = [img.get_rect(topleft=(self.X_POS, self.Y_POS)) for img in self.run_img]
        self.run_img_left = [pygame.transform.flip(img, True, False) for img in self.run_img]
        self.attack_img_left = [pygame.transform.flip(img, True, False) for img in self.attack_img]

        if self.X_POS > self.Player_X_POS:
            self.enemy_move_left = True
            self.enemy_move = False
            self.enemy_attack = False
            self.enemy_attack_left = False
            self.enemy_idle = False
            self.enemy_death = False
        elif self.X_POS < self.Player_X_POS:
            self.enemy_move_left = False
            self.enemy_move = False
            self.enemy_attack = False
            self.enemy_attack_left = False
            self.enemy_idle = False
            self.enemy_death = False

    def update(self):
        enemy_hitbox = self.enemy_hitbox[self.step_index % len(self.enemy_hitbox)]
        player_hitbox = self.Player_rect  # Zakładając, że Player_X_POS ma atrybut .rect
        if not enemy_hitbox.colliderect(player_hitbox):
            # Wróg się oddala od gracza
            if self.X_POS > self.Player_X_POS:
                self.enemy_move = True
                self.enemy_move_left = False
            else:
                self.enemy_move_left = True
                self.enemy_move = False

            self.enemy_attack = False
            self.enemy_idle = False
            self.enemy_death = False

        else:
            # Jeśli wróg jest blisko gracza
            if self.X_POS < self.Player_X_POS:
                self.enemy_move = False
                self.enemy_attack = True
                self.enemy_attack_left = False
                self.enemy_idle = False
                self.enemy_death = False
            elif self.X_POS >= self.Player_X_POS:
                self.enemy_move = False
                self.enemy_attack = False
                self.enemy_attack_left = True
                self.enemy_idle = False
                self.enemy_death = False
        if self.health < 0:
            self.enemy_move = False
            self.enemy_move_left = False
            self.enemy_attack = False
            self.enemy_attack_left = False
            self.enemy_idle = False
            self.enemy_death = True
        
        else:
            self.enemy_move = False
            self.enemy_move_left = False
            self.enemy_attack = False
            self.enemy_attack_left = True
            self.enemy_idle = True
            self.enemy_death = False
            
        if self.enemy_move:
            self.move()
        if self.enemy_move_left:
            self.move_left()
        if self.enemy_attack:
            self.attack()
        if self.enemy_attack_left:
            self.attack_left()
        if self.enemy_idle:
            self.idle()
        
    def move(self):
        self.image = self.run_img[self.step_index% len(self.run_img)]
        self.run_velocity = 15
        self.step_index += 1
        if self.step_index >= len(self.run_img):
            self.step_index = 0
    def move_left(self):
        self.image = self.run_img_left[self.step_index% len(self.run_img_left)]
        self.run_velocity = -15
        self.step_index += 1
        if self.step_index >= len(self.run_img):
            self.step_index = 0
    def attack(self):
        self.image = self.attack_img[self.step_index % len(self.attack_img)]
        self.step_index += 1
        if self.step_index >= len(self.run_img):
            self.step_index = 0
    def attack_left(self):
        self.image = self.attack_img_left[self.step_index % len(self.attack_img_left)]
        self.step_index += 1
        if self.step_index >= len(self.run_img):
            self.step_index = 0
    def idle(self):
        self.run_velocity = 0
        self.image = self.idle_img[self.step_index //8 % len(self.idle_img)]
        self.step_index += 1
        if self.step_index >= 8 * len(self.idle_img): 
            self.step_index = 0     



        