import pygame
from setting import Setting
from classGame.board import Board
from classGame.ball import Ball
from classGame.player import Player
from classGame.button import Button


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        self.bg = pygame.image.load(self.setting.bg_img)
        self.bg_rect = self.bg.get_rect()
        self.board = Board(self)
        self.ball = Ball(self)
        self.player = Player(self)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 20)
        self.button = Button(self, "Play")

    def runGame(self):
        while self.setting.active_game:
            self._checkEvents()
            self._checkbool()
            self._update()
            pygame.display.update()
            self.clock.tick(60)

    def check_button(self, mouse_pos):
        buttin_click = self.button.rect.collidepoint(mouse_pos)
        if buttin_click and not self.setting.active_button:
            self.setting.active_button = True
            pygame.mouse.set_visible(False)
        
    def _checkbool(self):
        if self.setting.active_shoot:
            self.ball.shoot()
        if not self.setting.active_one_shoot:
            if self.setting.active_up and self.setting.selected_y < self.screen.get_height()-250:
                self.setting.selected_y += 5
            if self.setting.active_down and self.setting.selected_y > 100:
                self.setting.selected_y -= 5
            if self.setting.active_right and self.setting.selected_x < self.screen.get_width():
                self.setting.selected_x += 5
            if self.setting.active_left and self.setting.selected_x > 100:
                self.setting.selected_x -= 5

    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.setting.active_game = False
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.setting.active_up = True
        elif event.key == pygame.K_DOWN:
            self.setting.active_down = True
        elif event.key == pygame.K_RIGHT:
            self.setting.active_right = True
        elif event.key == pygame.K_LEFT:
            self.setting.active_left = True
        elif event.key == pygame.K_SPACE:
            self.setting.active_shoot = True
            self.setting.active_one_shoot = True
        elif event.key == pygame.K_q:
            self.setting.active_game = False

    def _check_keyup_event(self, event):
        if event.key == pygame.K_UP:
            self.setting.active_up = False
        elif event.key == pygame.K_DOWN:
            self.setting.active_down = False
        elif event.key == pygame.K_RIGHT:
            self.setting.active_right = False
        elif event.key == pygame.K_LEFT:
            self.setting.active_left = False

    def _update(self):
        
        if self.setting.active_button:
            self.screen.blit(self.bg, self.bg_rect)
            self.board.draw_board()
            self.player.draw_player()
            self.ball.draw_helper()
            self.ball.draw_ball()
            self._show_score()
        else:
            self.button.draw_button()
        pygame.display.flip()

    def _show_score(self):
        self.screen.blit(self.font.render(
            f"Score: {self.setting.score}", True, (255, 0, 0)), (10, 10))


if __name__ == "__main__":
    play = Game()
    play.runGame()
