from pygame.sprite import Sprite
import pygame
import random
import math


class Ball(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.ball_img = pygame.image.load(self.setting.ball_img)
        self.rect = pygame.Rect(self.setting.ball_x, self.setting.ball_y,
                                self.setting.ball_width, self.setting.ball_height)

    def draw_helper(self):
        self.setting.road_ball = []
        for i in range(200):
            t = i / 200
            x = self.setting.ball_x + \
                (self.setting.selected_x - self.setting.ball_x +
                 self.setting.ball_width) * t
            y = self.setting.ball_y + \
                (-(self.setting.selected_y)) * math.sin(0.5 * 2 * math.pi * t)
            self.setting.road_ball.append((x, y))
        if not self.setting.active_shoot:
            for i in range(0, len(self.setting.road_ball) - 10, 2):
                pygame.draw.line(self.screen, (255, 99, 150),
                                 self.setting.road_ball[i], self.setting.road_ball[i + 1], 2)

    def reset_setting(self):
        self.rect = (self.setting.ball_x, self.setting.ball_y)
        self.setting.speed_shoot = 0
        self.setting.board_x = random.randint(400, 1100)
        self.setting.active_shoot = False
        self.setting.active_one_shoot = False
        self.setting.index_ball = 0
        self.setting.selected_x = 100
        self.setting.selected_y = 100
        self.setting.score_shoot = False

    def shoot(self):
        if not self.setting.score_shoot:
            self.rect = self.setting.road_ball[self.setting.index_ball]
        elif self.rect[1] < 600:
            self.rect = (self.rect[0], self.rect[1]+5)
        else:
            self.reset_setting()
            
        if self.setting.board_x + 10 < self.rect[0] < self.setting.board_x + self.setting.ball_width + 10 and 435 < self.rect[1] < 440 and not self.setting.score_shoot:
            self.setting.score += 10
            self.setting.score_shoot = True
                
            
        if self.setting.index_ball == len(self.setting.road_ball) - 1:
            self.setting.ball_lose += 1
            self.reset_setting()
        if not self.setting.score_shoot:
            self.setting.index_ball += 1

    def draw_ball(self):
        self.screen.blit(self.ball_img, self.rect)
