import pygame, json
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

        self.load_json = None

        self.player1_turn = False
        self.player2_turn = False
        self.player3_turn = False
        self.player4_turn = False

        self.player1_alive = True
        self.player2_alive = True
        self.player3_alive = True
        self.player4_alive = True

        self.player1_pos = int
        self.player2_pos = int
        self.player3_pos = int
        self.player4_pos = int

        self.scale = 2
        self.box_size = 0.5
        self.cellsize = 38
        self.cellcount = 12.6
        self.bordersize = 2
        self.boardlength = self.cellsize*self.cellcount + 100

        self.boardplacement =[[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                              [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                              [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                              [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                              [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                              [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                              [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                              [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                              [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                              [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]]
        
        for _ in range(1):
            # row 1 - cell list
            self.pos_1 = self.boardplacement[9][0][0]
            self.pos_2 = self.boardplacement[9][1][0]
            self.pos_3 = self.boardplacement[9][2][0]
            self.pos_4 = self.boardplacement[9][3][0]
            self.pos_5 = self.boardplacement[9][4][0]
            self.pos_6 = self.boardplacement[9][5][0]
            self.pos_7 = self.boardplacement[9][6][0]
            self.pos_8 = self.boardplacement[9][7][0]
            self.pos_9 = self.boardplacement[9][8][0]
            self.pos_10 = self.boardplacement[9][9][0]

            # row 2 - cell list
            self.pos_20 = self.boardplacement[8][0][0]
            self.pos_19 = self.boardplacement[8][1][0]
            self.pos_18 = self.boardplacement[8][2][0]
            self.pos_17 = self.boardplacement[8][3][0]
            self.pos_16 = self.boardplacement[8][4][0]
            self.pos_15 = self.boardplacement[8][5][0]
            self.pos_14 = self.boardplacement[8][6][0]
            self.pos_13 = self.boardplacement[8][7][0]
            self.pos_12 = self.boardplacement[8][8][0]
            self.pos_11 = self.boardplacement[8][9][0]

            # row 3 - cell list
            self.pos_21 = self.boardplacement[7][0][0]
            self.pos_22 = self.boardplacement[7][1][0]
            self.pos_23 = self.boardplacement[7][2][0]
            self.pos_24 = self.boardplacement[7][3][0]
            self.pos_25 = self.boardplacement[7][4][0]
            self.pos_26 = self.boardplacement[7][5][0]
            self.pos_27 = self.boardplacement[7][6][0]
            self.pos_28 = self.boardplacement[7][7][0]
            self.pos_29 = self.boardplacement[7][8][0]
            self.pos_30 = self.boardplacement[7][9][0]

            # row 4 - cell list
            self.pos_40 = self.boardplacement[6][0][0]
            self.pos_39 = self.boardplacement[6][1][0]
            self.pos_38 = self.boardplacement[6][2][0]
            self.pos_37 = self.boardplacement[6][3][0]
            self.pos_36 = self.boardplacement[6][4][0]
            self.pos_35 = self.boardplacement[6][5][0]
            self.pos_34 = self.boardplacement[6][6][0]
            self.pos_33 = self.boardplacement[6][7][0]
            self.pos_32 = self.boardplacement[6][8][0]
            self.pos_31 = self.boardplacement[6][9][0]

            # row 5 - cell list
            self.pos_41 = self.boardplacement[9][0][0]
            self.pos_42 = self.boardplacement[9][1][0]
            self.pos_43 = self.boardplacement[9][2][0]
            self.pos_44 = self.boardplacement[9][3][0]
            self.pos_45 = self.boardplacement[9][4][0]
            self.pos_46 = self.boardplacement[9][5][0]
            self.pos_47 = self.boardplacement[9][6][0]
            self.pos_48 = self.boardplacement[9][7][0]
            self.pos_49 = self.boardplacement[9][8][0]
            self.pos_50 = self.boardplacement[9][9][0]

            # row 6 - cell list
            self.pos_60 = self.boardplacement[8][0][0]
            self.pos_59 = self.boardplacement[8][1][0]
            self.pos_58 = self.boardplacement[8][2][0]
            self.pos_57 = self.boardplacement[8][3][0]
            self.pos_56 = self.boardplacement[8][4][0]
            self.pos_55 = self.boardplacement[8][5][0]
            self.pos_54 = self.boardplacement[8][6][0]
            self.pos_53 = self.boardplacement[8][7][0]
            self.pos_52 = self.boardplacement[8][8][0]
            self.pos_51 = self.boardplacement[8][9][0]

            # row 7- cell list
            self.pos_61 = self.boardplacement[9][0][0]
            self.pos_62 = self.boardplacement[9][1][0]
            self.pos_63 = self.boardplacement[9][2][0]
            self.pos_64 = self.boardplacement[9][3][0]
            self.pos_65 = self.boardplacement[9][4][0]
            self.pos_66 = self.boardplacement[9][5][0]
            self.pos_67 = self.boardplacement[9][6][0]
            self.pos_68 = self.boardplacement[9][7][0]
            self.pos_69 = self.boardplacement[9][8][0]
            self.pos_70 = self.boardplacement[9][9][0]

            # row 8 - cell list
            self.pos_80 = self.boardplacement[8][0][0]
            self.pos_79 = self.boardplacement[8][1][0]
            self.pos_78 = self.boardplacement[8][2][0]
            self.pos_77 = self.boardplacement[8][3][0]
            self.pos_76 = self.boardplacement[8][4][0]
            self.pos_75 = self.boardplacement[8][5][0]
            self.pos_74 = self.boardplacement[8][6][0]
            self.pos_73 = self.boardplacement[8][7][0]
            self.pos_72 = self.boardplacement[8][8][0]
            self.pos_71 = self.boardplacement[8][9][0]

            # row 9- cell list
            self.pos_81 = self.boardplacement[9][0][0]
            self.pos_82 = self.boardplacement[9][1][0]
            self.pos_83 = self.boardplacement[9][2][0]
            self.pos_84 = self.boardplacement[9][3][0]
            self.pos_85 = self.boardplacement[9][4][0]
            self.pos_86 = self.boardplacement[9][5][0]
            self.pos_87 = self.boardplacement[9][6][0]
            self.pos_88 = self.boardplacement[9][7][0]
            self.pos_89 = self.boardplacement[9][8][0]
            self.pos_90 = self.boardplacement[9][9][0]

            # row 10 - cell list
            self.pos_100 = self.boardplacement[8][0][0]
            self.pos_99 = self.boardplacement[8][1][0]
            self.pos_98 = self.boardplacement[8][2][0]
            self.pos_97 = self.boardplacement[8][3][0]
            self.pos_96 = self.boardplacement[8][4][0]
            self.pos_95 = self.boardplacement[8][5][0]
            self.pos_94 = self.boardplacement[8][6][0]
            self.pos_93 = self.boardplacement[8][7][0]
            self.pos_92 = self.boardplacement[8][8][0]
            self.pos_91 = self.boardplacement[8][9][0]

            # Vertical lines (self.box_size made them go all the way ?)
            self.vertical1 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical2 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical3 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical4 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical5 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical6 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical7 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical8 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical9 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical10 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical11 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical12 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical13 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical14 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical15 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical16 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical17 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical18 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical19 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical20 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))
            self.vertical21 = pygame.Surface((int(self.bordersize) * self.scale, int(self.boardlength) // self.box_size + int(self.bordersize) - 1))

            # Horizontal lines
            self.horizontal1 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal2 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal3 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal4 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal5 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal6 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal7 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal8 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal9 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal10 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal11 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal12 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal13 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal14 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal15 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal16 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal17 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal18 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal19 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))
            self.horizontal20 = pygame.Surface((int(self.boardlength) // self.box_size, int(self.bordersize) * self.scale))

        self.video_resolution = [(self.boardlength * 2, self.boardlength * 2),(1000, 1000), (1024, 760), (1280, 720)]
        self.DISPLAY_W, self.DISPLAY_H = self.video_resolution[0]
        #self.choice = 0
        #self.change_resolution = False
        self.MAIN = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.menucolours = [(80, 110, 100), (255, 190, 140), (220, 110, 255), (0, 0, 0)]
        self.HIGHLIGHTED, self.MENUCOLOUR, self.WHITE, self.BORDERCOLOUR = (120, 170, 60), self.menucolours[0], (255, 255, 255), (0, 0, 0)

        #self.player1 = Player1(self)

        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.videosettings_menu = VideoSettings(self)
        self.coloursettings_menu = MenuColourSettings(self)
        self.board = Board(self)
        self.current_menu = self.main_menu

    def load_setting(self):
        with open("game.json", "r") as file:
            return json.load(file)

    def save_settings(self):
            with open("game.json", "w") as file:
                json.dump(self, file)
    
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
    
    def draw_character(self):

        for lst in range(len(self.boardplacement)):
            for cell in range(int(self.boardplacement)):
                if cell == 1:
                    pass
                if cell == 2:
                    pass
                if cell == 3:
                    pass
                if cell == 4:
                    pass
        

    
    def reset_keys(self):
        self.ESCAPE_KEY, self.ENTER_KEY, self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.BACKSPACE_KEY = False, False, False, False, False, False, False

    def game_loop(self):
        while self.playing:
            self.load_json = self.load_setting()
            self.check_events()
            if self.ESCAPE_KEY:
                self.playing = False
            self.window.fill(self.MENUCOLOUR)
            #self.board.draw_boxes()
            #self.board.blit_board()

            #Check Player Placement
            self.position()

            #Draw Board
            self.draw_cells()

            # cell list
            #print(self.pos_1)

            #self.draw_text("We are inside the game!", 30, self.DISPLAY_W/2, self.DISPLAY_H/2) # between display resetting & main window blitting
            #self.window.blit(self.display_surface, (0, 0))

            #Draw cell numbers
            self.draw_cellnumbers()

            self.MAIN.blit(self.window, (100, 100))
            pygame.display.update()
            self.reset_keys()

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)
    
    def draw_boardtext(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    def draw_highlighted_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.HIGHLIGHTED)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    def draw_cells(self):
         for _ in range(12):
            scale = 2.5
            required_adjusting = int(self.cellsize * scale)
            saved = required_adjusting

            self.MAIN.fill(self.MENUCOLOUR)
            self.vertical1.fill(self.BORDERCOLOUR)
            self.vertical2.fill(self.BORDERCOLOUR)
            self.horizontal1.fill(self.BORDERCOLOUR)
            self.horizontal2.fill(self.BORDERCOLOUR)

            # row 1
            self.window.blit(self.vertical1, (0, 0))
            self.window.blit(self.vertical2, (int(self.cellsize * scale) - self.bordersize, 0))
            self.window.blit(self.vertical3, (int(self.cellsize * scale), 0))
            self.window.blit(self.vertical4, (int(self.cellsize * scale) * 2 - self.bordersize, 0))
            self.window.blit(self.vertical5, (int(self.cellsize * scale) * 2, 0))
            self.window.blit(self.vertical6, (int(self.cellsize * scale) * 3 - self.bordersize, 0))
            self.window.blit(self.vertical7, (int(self.cellsize * scale) * 3, 0))
            self.window.blit(self.vertical8, (int(self.cellsize * scale) * 4 - self.bordersize, 0))
            self.window.blit(self.vertical9, (int(self.cellsize * scale) * 4, 0))
            self.window.blit(self.vertical10, (int(self.cellsize * scale) * 5 - self.bordersize, 0))
            self.window.blit(self.vertical11, (int(self.cellsize * scale) * 5, 0))
            self.window.blit(self.vertical12, (int(self.cellsize * scale) * 6 - self.bordersize, 0))
            self.window.blit(self.vertical13, (int(self.cellsize * scale) * 6, 0))
            self.window.blit(self.vertical14, (int(self.cellsize * scale) * 7 - self.bordersize, 0))
            self.window.blit(self.vertical15, (int(self.cellsize * scale) * 7, 0))
            self.window.blit(self.vertical16, (int(self.cellsize * scale) * 8 - self.bordersize, 0))
            self.window.blit(self.vertical17, (int(self.cellsize * scale) * 8, 0))
            self.window.blit(self.vertical18, (int(self.cellsize * scale) * 9 - self.bordersize, 0))
            self.window.blit(self.vertical19, (int(self.cellsize * scale) * 9, 0))
            self.window.blit(self.vertical20, (int(self.cellsize * scale) * 10 - self.bordersize, 0))
            self.window.blit(self.vertical21, (int(self.cellsize * scale) * 10, 0))

            #row 2
            #self.window.blit(self.vertical25, (0, 0 + required_adjusting))
            #self.window.blit(self.vertical26, (int(self.cellsize * scale) - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical27, (int(self.cellsize * scale), 0 + required_adjusting))
            #self.window.blit(self.vertical28, (int(self.cellsize * scale) * 2 - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical29, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            #self.window.blit(self.vertical30, (int(self.cellsize * scale) * 3 - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical31, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            #self.window.blit(self.vertical32, (int(self.cellsize * scale) * 4 - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical33, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            #self.window.blit(self.vertical34, (int(self.cellsize * scale) * 5 - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical35, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            #self.window.blit(self.vertical36, (int(self.cellsize * scale) * 6 - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical37, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            #self.window.blit(self.vertical38, (int(self.cellsize * scale) * 7 - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical39, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            #self.window.blit(self.vertical40, (int(self.cellsize * scale) * 8 - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical41, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            #self.window.blit(self.vertical42, (int(self.cellsize * scale) * 9 - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical43, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            #self.window.blit(self.vertical44, (int(self.cellsize * scale) * 10 - self.bordersize, 0 + required_adjusting))
            #self.window.blit(self.vertical45, (int(self.cellsize * scale) * 10, 0 + required_adjusting))

            #column 1
            self.window.blit(self.horizontal1, (0, 0))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize))

            #column 2
            self.window.blit(self.horizontal1, (0, 0 + required_adjusting))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0 + required_adjusting))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize + required_adjusting))

            #column 3
            required_adjusting += saved
            self.window.blit(self.horizontal1, (0, 0 + required_adjusting))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0 + required_adjusting))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize + required_adjusting))

            #column 4
            required_adjusting += saved
            self.window.blit(self.horizontal1, (0, 0 + required_adjusting))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0 + required_adjusting))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize + required_adjusting))

            #column 5
            required_adjusting += saved
            self.window.blit(self.horizontal1, (0, 0 + required_adjusting))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0 + required_adjusting))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize + required_adjusting))

            #column 6
            required_adjusting += saved
            self.window.blit(self.horizontal1, (0, 0 + required_adjusting))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0 + required_adjusting))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize + required_adjusting))

            #column 7
            required_adjusting += saved
            self.window.blit(self.horizontal1, (0, 0 + required_adjusting))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0 + required_adjusting))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize + required_adjusting))

            #column 8
            required_adjusting += saved
            self.window.blit(self.horizontal1, (0, 0 + required_adjusting))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0 + required_adjusting))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize + required_adjusting))

            #column 9
            required_adjusting += saved
            self.window.blit(self.horizontal1, (0, 0 + required_adjusting))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0 + required_adjusting))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize + required_adjusting))

            #column 10
            required_adjusting += saved
            self.window.blit(self.horizontal1, (0, 0 + required_adjusting))
            self.window.blit(self.horizontal2, (0, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal3, (int(self.cellsize * scale), 0 + required_adjusting))
            self.window.blit(self.horizontal4, (int(self.cellsize * scale), int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal5, (int(self.cellsize * scale) * 2, 0 + required_adjusting))
            self.window.blit(self.horizontal6, (int(self.cellsize * scale) * 2, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal7, (int(self.cellsize * scale) * 3, 0 + required_adjusting))
            self.window.blit(self.horizontal8, (int(self.cellsize * scale) * 3, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal9, (int(self.cellsize * scale) * 4, 0 + required_adjusting))
            self.window.blit(self.horizontal10, (int(self.cellsize * scale) * 4, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal11, (int(self.cellsize * scale) * 5, 0 + required_adjusting))
            self.window.blit(self.horizontal12, (int(self.cellsize * scale) * 5, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal13, (int(self.cellsize * scale) * 6, 0 + required_adjusting))
            self.window.blit(self.horizontal14, (int(self.cellsize * scale) * 6, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal15, (int(self.cellsize * scale) * 7, 0 + required_adjusting))
            self.window.blit(self.horizontal16, (int(self.cellsize * scale) * 7, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal17, (int(self.cellsize * scale) * 8, 0 + required_adjusting))
            self.window.blit(self.horizontal18, (int(self.cellsize * scale) * 8, int(self.cellsize * scale) - self.bordersize + required_adjusting))
            self.window.blit(self.horizontal19, (int(self.cellsize * scale) * 9, 0 + required_adjusting))
            self.window.blit(self.horizontal20, (int(self.cellsize * scale) * 9, int(self.cellsize * scale) - self.bordersize + required_adjusting))

            required_adjusting = saved
            
    def draw_cellnumbers(self):
        scale = 2.5
        required_adjustion = self.cellsize * scale
        saved = required_adjustion
        vertical_adjustion = required_adjustion

        # Row 1
        self.draw_boardtext("100", 16, self.bordersize + 15, self.bordersize + 12)
        self.draw_boardtext("99", 16, required_adjustion + self.bordersize + 15, self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("98", 16, required_adjustion + self.bordersize + 15, self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("97", 16, required_adjustion + self.bordersize + 15, self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("96", 16, required_adjustion + self.bordersize + 15, self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("95", 16, required_adjustion + self.bordersize + 15, self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("94", 16, required_adjustion + self.bordersize + 15, self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("93", 16, required_adjustion + self.bordersize + 15, self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("92", 16, required_adjustion + self.bordersize + 15, self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("91", 16, required_adjustion + self.bordersize + 15, self.bordersize + 12)

        # Row 2
        self.draw_boardtext("90", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("89", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("88", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("87", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("86", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("85", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("84", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("83", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("82", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("81", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)

        # Row 3
        vertical_adjustion += saved
        self.draw_boardtext("80", 16, self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion = saved
        self.draw_boardtext("79", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("78", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("77", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("76", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("75", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("74", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("73", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("72", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("71", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)

        # Row 4
        vertical_adjustion += saved
        self.draw_boardtext("70", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("69", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("68", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("67", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("66", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("65", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("64", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("63", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("62", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("61", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)

        # Row 5
        vertical_adjustion += saved
        self.draw_boardtext("60", 16, self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion = saved
        self.draw_boardtext("59", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("58", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("57", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("56", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("55", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("54", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("53", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("52", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("51", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)

        # Row 6
        vertical_adjustion += saved
        self.draw_boardtext("50", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("49", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("48", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("47", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("46", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("45", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("44", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("43", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("42", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("41", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)

        # Row 7
        vertical_adjustion += saved
        self.draw_boardtext("40", 16, self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion = saved
        self.draw_boardtext("39", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("38", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("37", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("36", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("35", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("34", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("33", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("32", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("31", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)

        # Row 8
        vertical_adjustion += saved
        self.draw_boardtext("30", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -=saved
        self.draw_boardtext("29", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("28", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("27", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("26", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("25", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("24", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("23", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("22", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("21", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)

        # Row 9
        vertical_adjustion += saved
        self.draw_boardtext("20", 16, self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion = saved
        self.draw_boardtext("19", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("18", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("17", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("16", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("15", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("14", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("13", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("12", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion += saved
        self.draw_boardtext("11", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)

        # Row 10
        vertical_adjustion += saved
        self.draw_boardtext("10", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("9", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("8", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("7", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("6", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("5", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("4", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("3", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("2", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)
        required_adjustion -= saved
        self.draw_boardtext("1", 16, required_adjustion + self.bordersize + 15, vertical_adjustion + self.bordersize + 12)

    def position(self):
        player_position = list(self.load_json["Game"]["Players"]["Positions"].values())
        playerlist = []

        if self.player1_alive:
            playerlist.append(self.player1_pos)
        if self.player2_alive:
            playerlist.append(self.player2_pos)
        if self.player3_alive:
            playerlist.append(self.player3_pos)
        if self.player4_alive:
            playerlist.append(self.player4_pos)

        for player in playerlist:
            if player == self.player1_pos:
                self.player1_pos = player_position[0]
            elif player == self.player2_pos:
                self.player2_pos = player_position[1]
            elif player == self.player3_pos:
                self.player3_pos = player_position[2]
            elif player == self.player4_pos:
                self.player4_pos = player_position[3]
        
        print()
        print(f"self.player1_pos: {self.player1_pos}")
        print(f"self.player2_pos: {self.player2_pos}")
        print(f"self.player3_pos: {self.player3_pos}")
        print(f"self.player4_pos: {self.player4_pos}")
        print()
            
    def check_players(self):
        pass


class Board(Game):
    def __init__(self, game):
        #Game.__init__(self, game)
        self.game = game
        self.boxborder_horizontal = pygame.Rect(0, 0, 5, 5)
        self.boxborder_vertical = pygame.Rect(0, 0, 5, 5)
        self.BOXBORDERCOLOUR = (0, 0, 0)
        self.boxw, self.boxh = self.game.DISPLAY_W/12, self.game.DISPLAY_H/12
        pygame.Vector2(0,1)
        self.box_count = [12, 12]
        self.position_player1 = None
        self.position_player2 = None
        self.position_player3 = None
        self.position_player4 = None

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
