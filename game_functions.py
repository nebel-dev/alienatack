import sys
import pygame as pg
from bullet import Bullet
from alien import Alien


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update image on screen and switch to new screen"""
    # redraw the screen every time you circle
    screen.fill(ai_settings.bg_color)

    # Redraw all the bullets behind the ship and the alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
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


def get_number_aliens_x(ai_setting, alien_width):
    """calculate how many aliens a row can hold"""
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_setting, ship_height, alien_height):
    """calculate how many rows of aliens a screen can hold"""
    available_space_y = ai_setting.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    """create a alien and put it at present line"""
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_setting, screen, ship, aliens):
    """create a alien group"""
    # create a alien and calculate how many aliens a row can hold
    # the distance between aliens is alien's width
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)

    # create a alien group
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)





