from pygame.sprite import Sprite
import pygame


class Player(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.player_img = pygame.image.load(self.setting.player_img)
        self.rect = pygame.Rect(self.setting.player_x, self.setting.player_y,
                                self.setting.player_width, self.setting.player_height)

    def draw_player(self):
        self.screen.blit(self.player_img, self.rect)
