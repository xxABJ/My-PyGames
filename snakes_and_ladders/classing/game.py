import pygame
from menu import *

# gameclass - https://www.youtube.com/@CDcodes

# make a menu class that generates a menu on the pygame window.
# make a button class that generates buttons on the menu/other.
# make a game class? (prob have to draw the actual game.. maybe)

class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.ESCAPE_KEY, self.ENTER_KEY, self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.BACKSPACE_KEY = False, False, False, False, False, False, False
        self.video_resolution = [(800, 600), (1024, 760), (1280, 720)]
        self.DISPLAY_W, self.DISPLAY_H = self.video_resolution[0]
        #self.choice = 0
        #self.change_resolution = False
        self.display_surface = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.HIGHLIGHTED, self.MENUCOLOUR, self.WHITE = (120, 170, 60), (80, 110, 100), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.videosettings_menu = VideoSettings(self)
        self.current_menu = self.main_menu
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.current_menu.run_menu_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACKSPACE_KEY = True
    
    def reset_keys(self):
        self.ESCAPE_KEY, self.ENTER_KEY, self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.BACKSPACE_KEY = False, False, False, False, False, False, False

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.ESCAPE_KEY:
                self.playing = False
            self.display_surface.fill(self.MENUCOLOUR)
            self.draw_text("We are inside the game!", 30, self.DISPLAY_W/2, self.DISPLAY_H/2) # between display resetting & main window blitting
            self.window.blit(self.display_surface, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display_surface.blit(text_surface, text_rect)

    def draw_highlighted_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.HIGHLIGHTED)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display_surface.blit(text_surface, text_rect)
    