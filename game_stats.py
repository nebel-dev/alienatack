class GameStats:
    """track game statistics"""

    def __init__(self, ai_settings):
        """initialize statistics"""
        self.game_active = True
        self.ai_settings = ai_settings
        self.reset_stat()

    def reset_stat(self):
        """initializing statistics may change during the game"""
        self.ships_left = self.ai_settings.ship_limit

