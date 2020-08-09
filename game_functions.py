import sys
import pygame as pg
from bullet import Bullet


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """Response button"""
    if event.key == pg.K_RIGHT:
        ship.movement_right = True
    elif event.key == pg.K_LEFT:
        ship.movement_left = True
    elif event.key == pg.K_SPACE:
        # Create a bullet and add it to the group bullets
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key ==pg.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Response loosening"""
    if event.key == pg.K_RIGHT:
        ship.movement_right = False
    elif event.key == pg.K_LEFT:
        ship.movement_left = False


def check_events(ship, ai_settings, screen, bullets):
    """Monitor keyboard and mouse events"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, alien, bullets):
    """Update image on screen and switch to new screen"""
    # redraw the screen every time you circle
    screen.fill(ai_settings.bg_color)

    # Redraw all the bullets behind the ship and the alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    # Make the most recently drawn screen visible
    pg.display.flip()


def update_bullets(bullets):
    """update position of bullets and delete lost bullets"""
    # update position of bullets
    bullets.update()

    # delete lost bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


