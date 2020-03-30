import pygame


class Ship:

    def __init__(self, screen):
        """initialize the ship and set its initial position"""
        self.screen = screen

        # Loading ship image and obtaining its external rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # movement signs
        self.movement_right = False
        self.movement_left = False

    def update(self):
        if self.movement_right:
            # move the ship to the right
            self.rect.centerx += 1
        if self.movement_left:
            # move the ship to the left
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the ship at the designated location"""
        self.screen.blit(self.image, self.rect)
