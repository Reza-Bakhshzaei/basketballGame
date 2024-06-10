
class Setting:
    def __init__(self) -> None:
        # General Setting
        self.score = 0
        self.score_shoot = False
        self.selected_x = 100
        self.selected_y = 100
        self.screen_width = 1200
        self.screen_height = 690
        self.active_game = True
        self.active_button = False
        self.active_up = False
        self.active_down = False
        self.active_right = False
        self.active_left = False

        # Board
        self.board_width = 200
        self.board_height = 350
        self.board_x = 0
        self.board_y = 380

        # Ball
        self.road_ball = []
        self.index_ball = 0
        self.ball_width = 25
        self.ball_height = 25
        self.ball_x = 50
        self.ball_y = 525
        self.angel_shoot = 180
        self.speed_ball = 0.06
        self.active_shoot = False
        self.active_one_shoot = False

        # Player
        self.player_width = 260
        self.player_height = 100
        self.player_x = 25
        self.player_y = 425

        # Images
        self.bg_img = r".\files\bg.jpg"
        self.board_img = r".\files\board.png"
        self.ball_img = r".\files\ball.png"
        self.player_img = r".\files\player.png"
