import pygame 
import os 
import random 
pygame.init()

#Global constants 
screen_h = 600
screen_w = 1100

SCREEN = pygame.display.set_mode((screen_w, screen_h))

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))

#diving
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

#Obstacle images 

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

LARGE_CACTRUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                 pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                 pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

#Bird 
BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BACKGROUND = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340 #Y position of dino where diving/ducking 
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING 
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_velocity = self.JUMP_VELOCITY
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect() #makes an rectangular area to detect collision sized same as dino image
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino.jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput[pygame.K_w] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_s] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = True
        elif not (self.dino_jump or userInput[pygame.K_s]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
        
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_velocity * 4
            self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_jump = False
            self.jump_velocity = self.JUMP_VELOCITY
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = screen_w + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed          # Przesuwa obiekt w lewo z prędkością gry
        if self.x < -self.width:      # Jeśli obiekt całkiem zniknie z ekranu z lewej strony
            self.x = screen_w + random.randint(2500,3000)  # Teleportuje go na prawo za ekranem
            self.y = random.randint(50,100)                # Ustawia nową losową wysokość
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_w

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    

        



