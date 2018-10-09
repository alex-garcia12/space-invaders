import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien_st1
from alien import Alien_st2
from alien import Alien_st3
from alien import Alien_st4
import game_functions as gf
from game_stats import GameStats
from button import Button
from button import Startup
from button import First_Value
from button import Second_Value
from button import Third_Value
from button import Fourth_Value
from button import High_Score
from scoreboard import Scoreboard
from pygame.sprite import Group

def run_game():                                     #Here we initialize game and create a screen object
    pygame.init()                                   #this initializes background settings
    ai_settings = Settings()
    screen = pygame.display.set_mode\
    ((ai_settings.screen_width, ai_settings.screen_height)) #sets screen = settings attributes

    pygame.display.set_caption("Space Invaders")    #sets the name of the window

    play_button = Button(ai_settings, screen, "Play")   #make a play button
    start_screen = Startup(ai_settings, screen, "Space Invaders")
    first_value = First_Value(ai_settings, screen, " = 50")
    second_value = Second_Value(ai_settings, screen, " = 100")
    third_value = Third_Value(ai_settings, screen, " = 150")
    fourth_value = Fourth_Value(ai_settings, screen, " = ???")
    high_score = High_Score(ai_settings, screen, "High Scores")

    ship = Ship(ai_settings, screen)                #make a ship
    alien1 = Alien_st1(ai_settings, screen)
    alien2 = Alien_st2(ai_settings, screen)
    alien3 = Alien_st3(ai_settings, screen)
    alien4 = Alien_st4(ai_settings, screen)
    bullets = Group()                               #group where bullets are stored
    aliens = Group()                                #group where aliens are stored
    stats = GameStats(ai_settings)                  #create an instance to store game statistics
    sb = Scoreboard(ai_settings, screen, stats)     #instance that scores game stats and create a scoreboard

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:                                     #loop that controls events while the game is running
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)     #checks for player input

        if stats.game_active:                                       #check if game is still active (still have ships left)
            ship.update()                                           #updates ship's position
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  #updates bullets' positions
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, alien1, alien2, alien3, alien4, bullets,
                         play_button, start_screen, first_value, second_value, third_value, fourth_value, high_score)    #with updated positions of everything, draw new screens


run_game()