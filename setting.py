class Settings:
    """Class to store all setting"""

    def __init__(self):
        """initial game setting"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed_factor = 1.5
        self.ship_limit = 0

        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 is move right, -1 is move left
        self.fleet_direction = 1

        # speed up the pace of the game
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.bullets_allowed = 3
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction 为 1 表示向右;为 -1 表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """ 提高速度设置 """
        self.bullets_allowed += 1
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
