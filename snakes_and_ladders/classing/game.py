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
        self.DISPLAY_W, self.DISPLAY_H = self.video_resolution[1]
        #self.choice = 0
        #self.change_resolution = False
        self.display_surface = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.menucolours = [(80, 110, 100), (255, 190, 140), (220, 110, 255), (0, 0, 0)]
        self.HIGHLIGHTED, self.MENUCOLOUR, self.WHITE = (120, 170, 60), self.menucolours[0], (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.videosettings_menu = VideoSettings(self)
        self.coloursettings_menu = MenuColourSettings(self)
        self.board = Board(self)
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
            #self.display_surface.fill(self.MENUCOLOUR)
            self.board.draw_boxes()
            #self.board.blit_board()
            #self.draw_text("We are inside the game!", 30, self.DISPLAY_W/2, self.DISPLAY_H/2) # between display resetting & main window blitting
            #self.window.blit(self.display_surface, (0, 0))
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

class Board(Game):
    def __init__(self, game):
        #Game.__init__(self, game)
        self.game = game
        self.boxborder_horizontal = pygame.Rect(0, 0, 5, 5)
        self.boxborder_vertical = pygame.Rect(0, 0, 5, 5)
        self.BOXBORDERCOLOUR = (0, 0, 0)
        self.boxw, self.boxh = self.game.DISPLAY_W/12, self.game.DISPLAY_H/12
        self.box_count = [12, 12]

    def blit_board(self):
        self.game.window.blit(self.game.display_surface, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def draw_boxes(self):
        for row in range(self.box_count[0]):
            r = pygame.draw.rect(self.game.display_surface, self.BOXBORDERCOLOUR, self.boxborder_vertical)
            self.game.display_surface.fill(self.game.MENUCOLOUR)
            self.game.window.blit(self.game.display_surface, r)
            pygame.display.update()
            self.boxborder_vertical.x += self.boxh
            for column in range(self.box_count[1]):
                pygame.draw.rect(self.game.display_surface, self.BOXBORDERCOLOUR, self.boxborder_vertical)
                self.boxborder_vertical.y += self.boxw

    def draw_board(self):
        self.draw_boxes()
