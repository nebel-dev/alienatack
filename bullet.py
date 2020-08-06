import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class that manages the bullets fired by a ship"""

    def __init__(self, ai_setting, screen, ship):
        """creat a bullet object in the position of ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a rectangle at (0,0) to represent the bullet, and then set the correct position
        self.rect = pg.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet position in decimal
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """move the bullet up"""

        # Update the small value indicating the bullet position
        self.y -= self.speed_factor
        # Update the location of the rect that represents the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet in the screen"""
        pg.draw.rect(self.screen, self.color, self.rect)

