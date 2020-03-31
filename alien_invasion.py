import pygame as pg
from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # initial game and create a screen object
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(screen, ai_settings)
    # start game loop
    while True:
        # Monitor keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()

