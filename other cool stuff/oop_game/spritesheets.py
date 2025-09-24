import pygame
import os 
class Spritesheet():
    def __init__(self,filename,tile_width,tile_height,scale):
        # Loading all spritesheet
        #convert alpha method loads image faster and uses alpha channel
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.scale = scale
        self.tile_width = tile_width
        self.tile_height = tile_height

        self.sprites = self.load_sprites()
    
    def load_sprites(self):
        sprites = []

        sheet_width = self.sheet.get_width()
        sheet_height = self.sheet.get_height()

        #dividng spritesheet into rows and colums by dividing spritesheet width and height by sprite width and height (16x16)
        cols =  sheet_width // self.tile_width
        rows =  sheet_height // self.tile_height


        for y in range(rows):
            for x in range (cols):
                sprite = self.get_sprite(
                    x * self.tile_width,
                    y * self.tile_height,
                    self.tile_width,
                    self.tile_height
                )
                sprite = pygame.transform.scale(sprite, (self.tile_width * self.scale, self.tile_height * self.scale))
                sprites.append(sprite)
        return sprites    
    
    def get_sprite(self, x , y , width, height):
        #cut one sprite from given coordinats
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y , width, height))
        return sprite
    def get_all_sprites(self):
        return self.sprites

    def get_cols(self):
        return self.sheet.get_width() // self.tile_width
    def get_rows(self):
        return self.sheet.get_height() // self.tile_height
    