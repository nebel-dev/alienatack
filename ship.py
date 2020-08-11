import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        """initialize the ship and set its initial position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_setting = ai_settings

        # Loading ship image and obtaining its external rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimals in the ship's attribute "center"
        self.center = float(self.rect.centerx)

        # movement signs
        self.movement_right = False
        self.movement_left = False

    def update(self):
        if self.movement_right and self.rect.right < self.screen_rect.right:
            # move the ship to the right
            self.center += self.ai_setting.ship_speed_factor
        if self.movement_left and self.rect.left > 0:
            # move the ship to the left
            self.center -= self.ai_setting.ship_speed_factor

        # according to "self.center" to update "self.rect.centerx"
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at the designated location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """put ship in low center of screen"""
        self.center = self.screen_rect.centerx
