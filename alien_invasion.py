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
    # create a alien group
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Create a group to store bullets
    bullets = Group()

    # start game loop
    while True:
        # Monitor keyboard and mouse events
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets))
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()

