import pygame.ftfont

class Button():
    def __init__(self, ai_settings, screen, msg):
        #initialize button attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set the dimensions and properties of the button
        self.width, self.height = 80, 150
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)   #use default font and size 48

        #Build the button's rect object and center it
        self.rect = pygame.Rect((self.screen_rect.width / 2) - 30, self.screen_rect.height * 0.85, self.width, self.height)  #make a rect the same size as the button
        #self.rect.center = self.screen_rect.center                #center the button

        #the button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        #turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)    #turns text into image
        self.msg_image_rect = self.msg_image.get_rect()     #creat a rect from the image and center it to match the button's
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draw blanks button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Startup():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = self.screen_rect.width
        self.height = self.screen_rect.height

        self.startup_color = (0, 0, 0)
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 150)

        self.rect = pygame.Rect(0, 0, self.width, self.height / 2)
        #self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        # turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.startup_color)  # turns text into image
        self.msg_image_rect = self.msg_image.get_rect()  # creat a rect from the image and center it to match the button's
        self.msg_image_rect.center = self.rect.center

    def draw_start(self):
        # draw blanks button and then draw message
        self.screen.fill(self.startup_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class First_Value():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 30
        self.height = 10

        self.startup_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect((self.screen_rect.width / 2) + 20, self.screen_rect.height / 2, self.width, self.height)
        #self.rect.center = self.screen_rect.width / 2

        self.prep_msg(msg)

    def prep_msg(self, msg):
        # turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.startup_color)  # turns text into image
        self.msg_image_rect = self.msg_image.get_rect()  # creat a rect from the image and center it to match the button's
        self.msg_image_rect.center = self.rect.center

    def draw_value(self):
        # draw blanks button and then draw message
        self.screen.fill(self.startup_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Second_Value():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 30
        self.height = 10

        self.startup_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect((self.screen_rect.width / 2) + 29, (self.screen_rect.height / 2) + 40, self.width, self.height)
        #self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        # turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.startup_color)  # turns text into image
        self.msg_image_rect = self.msg_image.get_rect()  # creat a rect from the image and center it to match the button's
        self.msg_image_rect.center = self.rect.center

    def draw_value(self):
        # draw blanks button and then draw message
        self.screen.fill(self.startup_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Third_Value():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 30
        self.height = 10

        self.startup_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect((self.screen_rect.width / 2) + 29, (self.screen_rect.height / 2) + 80, self.width, self.height)
        #self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        # turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.startup_color)  # turns text into image
        self.msg_image_rect = self.msg_image.get_rect()  # creat a rect from the image and center it to match the button's
        self.msg_image_rect.center = self.rect.center

    def draw_value(self):
        # draw blanks button and then draw message
        self.screen.fill(self.startup_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Fourth_Value():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 30
        self.height = 10

        self.startup_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect((self.screen_rect.width / 2) + 30, (self.screen_rect.height / 2) + 120, self.width, self.height)
        #self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        # turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.startup_color)  # turns text into image
        self.msg_image_rect = self.msg_image.get_rect()  # creat a rect from the image and center it to match the button's
        self.msg_image_rect.center = self.rect.center

    def draw_value(self):
        # draw blanks button and then draw message
        self.screen.fill(self.startup_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class High_Score():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 50
        self.height = 20

        self.startup_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect((self.screen_rect.width / 2) - 30, self.screen_rect.height / 1.25, self.width, self.height)
        #self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        # turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.startup_color)  # turns text into image
        self.msg_image_rect = self.msg_image.get_rect()  # creat a rect from the image and center it to match the button's
        self.msg_image_rect.center = self.rect.center

    def draw_value(self):
        # draw blanks button and then draw message
        self.screen.fill(self.startup_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)