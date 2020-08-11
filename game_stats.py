class GameStats:
    """track game statistics"""

    def __init__(self, ai_settings):
        """initialize statistics"""
        self.game_active = False
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """initializing statistics may change during the game"""
        self.ships_left = self.ai_settings.ship_limit

