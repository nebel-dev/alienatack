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
        self.bullet_speed_factor = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 is move right, -1 is move left
        self.fleet_direction = 1


