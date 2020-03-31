import sys
import pygame as pg


def check_keydown_events(event, ship):
    """Response button"""
    if event.key == pg.K_RIGHT:
        ship.movement_right = True
    elif event.key == pg.K_LEFT:
        ship.movement_left = True


def check_keyup_events(event, ship):
    """Response loosening"""
    if event.key == pg.K_RIGHT:
        ship.movement_right = False
    elif event.key == pg.K_LEFT:
        ship.movement_left = False


def check_events(ship):
    """Monitor keyboard and mouse events"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Update image on screen and switch to new screen"""
    # redraw the screen every time you circle
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pg.display.flip()
