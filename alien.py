import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """class representing a single alien"""

    def __init__(self, ai_settings, screen):
        """initialize alien and start position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and set  its rect property
        self.image = pg.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alien start position is near the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the exact location of the alien
        self.x = float(self.rect.x)

    def blitme(self):
        """draw aliens at designated locations"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move aliens to the right or left"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """if aliens are on the edge of the screen, return 'True'"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
