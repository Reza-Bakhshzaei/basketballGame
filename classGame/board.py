from pygame.sprite import Sprite
import pygame, random

class Board(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.board_img = pygame.image.load(self.setting.board_img)
        self.setting.board_x = self.board_x = random.randint(400,1100)
        self.rect = pygame.Rect(self.board_x,self.setting.board_y,self.setting.board_width, self.setting.board_height)
        
    def draw_board(self):
        self.screen.blit(self.board_img, self.rect)
        
