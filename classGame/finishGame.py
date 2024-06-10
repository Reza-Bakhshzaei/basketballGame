import pygame.font

class Finished:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 500,150
        self.setting = ai_game.setting
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None,100)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_image(self):
        if self.setting.ball_lose >= 3:
            self.button_color = (255, 0, 0)
            self.msg = "Game Over!!"
        else:
             self.button_color = (0, 255, 0)
             self.msg = "Wine!!!"
        self._prep_msg(self.msg)
        self.setting.active_button = False
        self.setting.game_finish = True
        self.screen.fill(self.button_color,  self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)