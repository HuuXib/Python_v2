import pygame
import os

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


BACKGROUND_FOREST_BACK = pygame.image.load(os.path.join("assets/parallax_forest_pack/layers","parallax-forest-back-trees.png"))
BACKGROUND_FOREST_MID = pygame.image.load(os.path.join("assets/parallax_forest_pack/layers","parallax-forest-middle-trees.png"))
BACKGROUND_FOREST_FRONT = pygame.image.load(os.path.join("assets/parallax_forest_pack/layers","parallax-forest-front-trees.png"))
BACKGROUND_FOREST_LIGHT = pygame.image.load(os.path.join("assets/parallax_forest_pack/layers","parallax-forest-lights.png"))



class Warrior:
    
    X_POS = 80 
    Y_POS = 310
    step_index = 6
    
    RUN_VELOCITY = 30

    def __init__(self):
        self.step_index = 0
        self.move_img = MOVING
        self.run_img = RUNNING
        self.attack_img = ATTACK
        self.idle_img = IDLE
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
        prev_state = (self.warrior_move, self.warrior_run, self.warrior_attack, self.warrior_idle)


        if (userInput[pygame.K_a] or userInput[pygame.K_d]) and userInput[pygame.K_LSHIFT]:
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
            self.move()
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
    def move(self):
        self.image = self.run_img[self.step_index  % len(self.run_img)]
        self.warrior_rect.x += self.run_velocity
        self.step_index += 1
    def moveback(self):
        self.image = self.run_img_left[self.step_index  % len(self.run_img_left)]
        self.warrior_rect.x -= self.run_velocity
        self.step_index += 1
    def idle(self):
        self.image = self.idle_img[self.step_index  // 3 % len(self.idle_img)]
        self.step_index += 1
    def attack(self):
        self.image = self.attack_img[self.step_index  % len(self.attack_img)]
        self.step_index += 1


class Background():
    def __init__(self, screen_width, screen_height):
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

        self.back_speed = 1
        self.mid_speed = 2
        self.front_speed = 3
        self.light_speed = 0.5
    def update(self, player_velocity):
        self.back_x -= self.back_speed * player_velocity
        self.mid_x -= self.mid_speed * player_velocity
        self.front_x -= self.front_speed * player_velocity


        #zapetlanie obrazkow

        screen_width = self.back_trees.get_width()
        self.back_x %= screen_width
        self.mid_x %= screen_width
        self.front_x %= screen_width
        self.light_x %= screen_width


    def draw(self, screen):
        screen.blit(self.back_trees, (self.back_x, 0))
        screen.blit(self.back_trees, (self.back_x + self.back_trees.get_width(), 0))
        screen.blit(self.mid_trees, (self.mid_x, 0))
        screen.blit(self.mid_trees, (self.mid_x + self.mid_trees.get_width(), 0))
        screen.blit(self.front_trees, (self.front_x, 0))
        screen.blit(self.front_trees, (self.front_x + self.front_trees.get_width(), 0))
        screen.blit(self.light, (self.light_x, 0))
        screen.blit(self.light, (self.light_x + self.light.get_width(), 0))







        