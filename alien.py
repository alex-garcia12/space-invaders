import pygame
from pygame.sprite import Sprite

class Alien1(Sprite):
    def __init__(self, ai_settings, screen):                    #initialize the alien and its starting position
        super(Alien1, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.images = []
        self.images.append(pygame.image.load('images/alien1-1.png'))
        self.images.append(pygame.image.load('images/alien1-1.png'))
        self.images.append(pygame.image.load('images/alien1-2.png'))
        self.images.append(pygame.image.load('images/alien1-2.png'))



        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        #self.image = pygame.image.load('images/Alien.png')     #load the alien image and its rect attribute
        #self.rect = self.image.get_rect()

        self.rect.x = self.rect.width                           #start each new alien at the topleft of the screen
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)                             #store the alien's exact position

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:                #check if alien right rect is at the screen's right rect
            return True
        elif self.rect.left <= 0:                               #check if alien left rect is at the screen's left rect
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien2(Sprite):
    def __init__(self, ai_settings, screen):                    #initialize the alien and its starting position
        super(Alien2, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.images = []
        self.images.append(pygame.image.load('images/alien2-1.png'))
        self.images.append(pygame.image.load('images/alien2-1.png'))
        self.images.append(pygame.image.load('images/alien2-2.png'))
        self.images.append(pygame.image.load('images/alien2-2.png'))



        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        #self.image = pygame.image.load('images/Alien.png')     #load the alien image and its rect attribute
        #self.rect = self.image.get_rect()

        self.rect.x = self.rect.width                           #start each new alien at the topleft of the screen
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)                             #store the alien's exact position

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:                #check if alien right rect is at the screen's right rect
            return True
        elif self.rect.left <= 0:                               #check if alien left rect is at the screen's left rect
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien3(Sprite):
    def __init__(self, ai_settings, screen):                    #initialize the alien and its starting position
        super(Alien3, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.images = []
        self.images.append(pygame.image.load('images/alien3-1.png'))
        self.images.append(pygame.image.load('images/alien3-1.png'))
        self.images.append(pygame.image.load('images/alien3-2.png'))
        self.images.append(pygame.image.load('images/alien3-2.png'))



        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        #self.image = pygame.image.load('images/Alien.png')     #load the alien image and its rect attribute
        #self.rect = self.image.get_rect()

        self.rect.x = self.rect.width                           #start each new alien at the topleft of the screen
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)                             #store the alien's exact position

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:                #check if alien right rect is at the screen's right rect
            return True
        elif self.rect.left <= 0:                               #check if alien left rect is at the screen's left rect
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien4(Sprite):
    def __init__(self, ai_settings, screen):                    #initialize the alien and its starting position
        super(Alien4, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.images = []
        self.images.append(pygame.image.load('images/alien4-1.png'))
        self.images.append(pygame.image.load('images/alien4-1.png'))
        self.images.append(pygame.image.load('images/alien4-2.png'))
        self.images.append(pygame.image.load('images/alien4-2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        #self.image = pygame.image.load('images/Alien.png')     #load the alien image and its rect attribute
        #self.rect = self.image.get_rect()

        self.rect.x = self.rect.width                           #start each new alien at the topleft of the screen
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)                             #store the alien's exact position

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:                #check if alien right rect is at the screen's right rect
            return True
        elif self.rect.left <= 0:                               #check if alien left rect is at the screen's left rect
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Alien_st1():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/Alien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = (self.screen_rect.width / 2) - 30
        self.rect.centery = (self.screen_rect.height / 2) + 5

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien_st2():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien2-1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = (self.screen_rect.width / 2) - 30
        self.rect.centery = (self.screen_rect.height / 2) + 45

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien_st3():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien3-1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = (self.screen_rect.width / 2) - 30
        self.rect.centery = (self.screen_rect.height / 2) + 85

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien_st4():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien4-1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = (self.screen_rect.width / 2) - 30
        self.rect.centery = (self.screen_rect.height / 2) + 125

    def blitme(self):
        self.screen.blit(self.image, self.rect)