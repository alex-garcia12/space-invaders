import sys
import pygame
from bullet import Bullet
from alien import Alien1
from alien import Alien2
from alien import Alien3
from alien import Alien4
from time import sleep


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):     #respond to ship being hit by alien
    pygame.mixer.music.load('sounds/ship_explode.wav')
    pygame.mixer.music.play(1)

    if stats.ships_left > 0:
        stats.ships_left -= 1           #decrement ships_left

        #update scoreboard
        sb.prep_ships()

        #empty the list of aliens and bullets (remove them from the screen)
        aliens.empty()
        bullets.empty()

        #create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_high_score(stats, sb):
    #check to see if there's a new high score
    if stats.score > stats.high_score:          #check the current store vs the high score
        stats.high_score = stats.score
        sb.prep_high_score()


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width  #calculate the horizontal space available for aliens
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien1(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien1(ai_settings, screen)                              #create an alien and place it in the row
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_alien2(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien2(ai_settings, screen)                              #create an alien and place it in the row
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_alien3(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien3(ai_settings, screen)                              #create an alien and place it in the row
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_alien4(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien4(ai_settings, screen)                              #create an alien and place it in the row
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

# def create_alien42(ai_settings, screen, aliens):
#     alien = Alien4(ai_settings, screen)                              #create an alien and place it in the row
#     alien_width = alien.rect.width
#     alien.x = alien_width
#     alien.rect.x = alien.x
#     alien.rect.y = alien.rect.height + 2
#     aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    alien1 = Alien1(ai_settings, screen)                              #create an alien before calculations
    alien2 = Alien2(ai_settings, screen)
    alien3 = Alien3(ai_settings, screen)
    alien4 = Alien4(ai_settings, screen)
    number_aliens1_x = get_number_aliens_x(ai_settings, alien1.rect.width)
    number_aliens2_x = get_number_aliens_x(ai_settings, alien2.rect.width)
    number_aliens3_x = get_number_aliens_x(ai_settings, alien3.rect.width)
    number_aliens4_x = get_number_aliens_x(ai_settings, alien4.rect.width)

    number_rows = get_number_rows(ai_settings, ship.rect.height, alien1.rect.height)

    for row_number in range(5):
        if row_number == 1:
            for alien_number in range(number_aliens1_x):
                create_alien1(ai_settings, screen, aliens, alien_number, row_number)
        elif row_number == 2:
            for alien_number in range(number_aliens2_x):
                create_alien2(ai_settings, screen, aliens, alien_number, row_number)
        elif row_number == 3:
            for alien_number in range(number_aliens3_x):
                create_alien3(ai_settings, screen, aliens, alien_number, row_number)
        elif row_number == 4:
            for alien_number in range(number_aliens4_x):
                create_alien4(ai_settings, screen, aliens, alien_number, row_number)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)          #create a new bullet and add it to the bullets group
            bullets.add(new_bullet)                                 #store the new bullet in the bullets group


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:                                 #if the right arrow key is pressed...
        ship.moving_right = True                                    #Set the flag = true to get the ship to move right
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:                                #when spacebar is pressed...
        pygame.mixer.music.load('sounds/shoot1.wav')
        pygame.mixer.music.play(1)
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:     #when the right arrow key is released...
        ship.moving_right = False       #flag is set to false and the ship stops moving
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():            #check for events from the user
        if event.type == pygame.QUIT:           #if the upper right close button is clicked...
            sys.exit()                          #close the game

        elif event.type == pygame.MOUSEBUTTONDOWN:      #detects mouse clicks
            mouse_x, mouse_y = pygame.mouse.get_pos()   #saves coordinates of mouseclick
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:      #event loop responds when pygame detects a keydown event
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:        #event loop responds when pygame detects a keyup event
            check_keyup_events(event, ship)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    #start a new game when the player clicks Play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)    #flag that stores true or false
    if button_clicked and not stats.game_active:     #if collision of mouseclick hits play_button
        #reset the game settings
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)              #hide the mouse cursor

        #reset the game stats
        stats.reset_stats()                                 #gives player 3 new ships
        stats.game_active = True                            #start the game

        #reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    alien_collisions1 = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #ship_collisions = pygame.sprite.groupcollide(bullets, ship, True, True)

    if alien_collisions1:                                  #if a bullet hits an alien...
        pygame.mixer.music.load('sounds/alien_explode.wav')
        pygame.mixer.music.play(1)
        for aliens in alien_collisions1.values():
            stats.score += ai_settings.alien1_points     #add points to score    * len(aliens)
            sb.prep_score()                             #create new image to update the score
        check_high_score(stats, sb)

    # if len(aliens) == 44:
    #     create_alien42(ai_settings, screen, aliens)

    if len(aliens) == 0:  # check if the aliens group is empty
        # destroy existing bullets, speedup game, and create new fleet
        bullets.empty()
        ai_settings.increase_speed()

        #increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)  # fill it with aliens again


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():  # lets us modify bullets inside the loop
        if bullet.rect.bottom <= 0:  # check to see if the bullet has disappeared off the top of the screen
            bullets.remove(bullet)  # if it has, remove the bullets
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    #respond appropriately if any aliens have reached an edge
    for alien in aliens.sprites():
        if alien.check_edges():                     #loop through aliens and see if an alien has reached an edge

            change_fleet_direction(ai_settings, aliens) #if it has, whole fleet changes direction
            break


def change_fleet_direction(ai_settings, aliens):
    #drop the entire fleet and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed    #drop each alien by its drop speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #check if any aliens have reached the bottom
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #treat this the same as if the ship got hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

    if pygame.sprite.spritecollideany(ship, aliens):    #looks to see if anything in group alien has collided with sprite ship
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, alien1, alien2, alien3, alien4, bullets, play_button,
                  start_screen, first_value, second_value, third_value, fourth_value, high_score):
    screen.fill(ai_settings.bg_color)           #redraw the screen during each pass through the loop

    for bullet in bullets.sprites():            #here bullets.sprites returns a list of sprites in the group bullets
        bullet.draw_bullet()                    #we loop through each sprite in the group and draw each one

    #draw the score information
    sb.show_score()

    ship.blitme()                               #draw the ship after the background so the ship is on top of the bg
    aliens.draw(screen)

    #draw the play button if the game is inactive
    if not stats.game_active:
        start_screen.draw_start()
        first_value.draw_value()
        second_value.draw_value()
        third_value.draw_value()
        fourth_value.draw_value()
        high_score.draw_value()
        play_button.draw_button()
        alien1.blitme()
        alien2.blitme()
        alien3.blitme()
        alien4.blitme()

    pygame.display.flip()                       #tells pygame to make the most recently drawn screen visible
