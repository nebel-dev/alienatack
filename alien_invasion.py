import pygame as pg
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # initial game and create a screen object
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(screen, ai_settings)
    # Create a group to store bullets
    bullets = Group()

    # start game loop
    while True:
        # Monitor keyboard and mouse events
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

