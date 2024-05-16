from pygame.sprite import Sprite
import pygame

class Ball(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.ball_img = pygame.image.load(self.setting.ball_img)
        self.rect = pygame.Rect(50,525,self.setting.ball_width,self.setting.ball_height)
    

    def shoot(self):
        self.rect.x += self.setting.speed_shoot
        if self.rect.x >= self.setting.board_x:
            self.rect.x = 50
    def draw_ball(self):
        self.screen.blit(self.ball_img, self.rect)
        
