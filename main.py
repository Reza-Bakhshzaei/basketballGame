import pygame
from setting import Setting
from classGame.board import Board
from classGame.ball import Ball
from classGame.player import Player
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        self.bg = pygame.image.load(self.setting.bg_img)
        self.bg_rect = self.bg.get_rect()
        self.board = Board(self)
        self.ball = Ball(self)
        self.player = Player(self)
    
    def runGame(self):
        while self.setting.active_game:
            self._checkEvents()
            if self.setting.active_shoot:
                self.setting.speed_shoot += 0.01
            if self.setting.speed_shoot != 0 and not self.setting.active_shoot:
                self.ball.shoot()
            self._update()
            pygame.display.update()
            
    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.setting.active_game = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.setting.active_up = True
        elif event.key == pygame.K_DOWN:
            self.setting.active_down = True
        elif event.key == pygame.K_SPACE:
            self.setting.active_shoot = True
        elif event.key == pygame.K_q:
            self.setting.active_game = False
            

    def _check_keyup_event(self, event):
        if event.key == pygame.K_UP:
            self.setting.active_up = False
        elif event.key == pygame.K_DOWN:
            self.setting.active_down = False
        elif event.key == pygame.K_SPACE:
            self.setting.active_shoot = False
    
    
    def _update(self):
        
        self.screen.blit(self.bg, self.bg_rect)
        self.board.draw_board()
        self.player.draw_player()
        self.ball.draw_ball()
        pygame.display.flip()

if __name__ == "__main__":
    play = Game()
    play.runGame()