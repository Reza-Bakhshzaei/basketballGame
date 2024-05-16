
class Setting:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 690
        self.board_width = 200
        self.board_height = 350
        self.board_x = 0
        self.board_y = 380
        self.ball_width = 25
        self.ball_height = 25
        self.player_width = 260
        self.player_height = 100
        self.speed_shoot = 0
        self.active_game = True
        self.active_up = False
        self.active_down = False
        self.active_shoot = False
        self.bg_img = r"D:\PyProject\game project\basketballGame\files\bg.jpg"
        self.board_img = r"D:\PyProject\game project\basketballGame\files\board.png"
        self.ball_img = r"D:\PyProject\game project\basketballGame\files\ball.png"
        self.player_img = r"D:\PyProject\game project\basketballGame\files\player.png"