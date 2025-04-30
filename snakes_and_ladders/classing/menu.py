import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_menu_display = True
        self.highlightedx, self.highlightedy = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 10
        self.selected = ""

    def draw_selected(self):
        self.game.draw_highlighted_text(self.selected, 34, self.highlightedx, self.highlightedy)

    def blit_menu(self):
        self.game.window.blit(self.game.display_surface, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Main Menu Start Game"
        self.startx, self.starty = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 10
        self.optionsx, self.optionsy = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 50
        self.creditsx, self.creditsy = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 90
        self.selected = "Start Game"

    def display_menu(self):
        self.run_menu_display = True
        while self.run_menu_display:
            self.game.check_events()
            self.check_input()
            self.game.display_surface.fill(self.game.MENUCOLOUR)
            self.game.draw_text("Main Menu", 36, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 200)
            if self.selected == "Start Game":
                self.draw_selected()
                self.game.draw_text("Options", 30, self.optionsx, self.optionsy)
                self.game.draw_text("Credits", 30, self.creditsx, self.creditsy)
            elif self.selected == "Options":
                self.game.draw_text("Start Game", 30, self.startx, self.starty)
                self.draw_selected()
                self.game.draw_text("Credits", 30, self.creditsx, self.creditsy)
            elif self.selected == "Credits":
                self.game.draw_text("Start Game", 30, self.startx, self.starty)
                self.game.draw_text("Options", 30, self.optionsx, self.optionsy)
                self.draw_selected()
            self.blit_menu()

    def move_selection(self):
        if self.game.DOWN_KEY:
            if self.state == "Main Menu Start Game":
                self.highlightedx, self.highlightedy = self.optionsx, self.optionsy
                self.selected = "Options"
                self.state = "Main Menu Options"
            elif self.state == "Main Menu Options":
                self.highlightedx, self.highlightedy = self.creditsx, self.creditsy
                self.selected = "Credits"
                self.state = "Main Menu Credits"
            elif self.state == "Main Menu Credits":
                self.highlightedx, self.highlightedy = self.startx, self.starty
                self.selected = "Start Game"
                self.state = "Main Menu Start Game"
        elif self.game.UP_KEY:
            if self.state == "Main Menu Start Game":
                self.highlightedx, self.highlightedy = self.creditsx, self.creditsy
                self.selected = "Credits"
                self.state = "Main Menu Credits"
            elif self.state == "Main Menu Credits":
                self.highlightedx, self.highlightedy = self.optionsx, self.optionsy
                self.selected = "Options"
                self.state = "Main Menu Options"
            elif self.state == "Main Menu Options":
                self.highlightedx, self.highlightedy = self.startx, self.starty
                self.selected = "Start Game"
                self.state = "Main Menu Start Game"
    
    def check_input(self):
        self.move_selection()
        if self.game.ENTER_KEY:
            if self.state == "Main Menu Start Game":
                self.game.playing = True
            elif self.state == "Main Menu Options":
                self.game.current_menu = self.game.options_menu
            elif self.state == "Main Menu Credits":
                self.game.current_menu = self.game.credits_menu
            self.run_menu_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Options Video Settings"
        self.videox, self.videoy = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 10
        self.soundx, self.soundy = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 50
        self.menucolourx, self.menucoloury = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 90
        self.selected = "Video Settings"

    def display_menu(self):
        self.run_menu_display = True
        while self.run_menu_display:
            self.game.check_events()
            self.check_input()
            self.game.display_surface.fill(self.game.MENUCOLOUR)
            self.game.draw_text("Options", 36, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 200)
            if self.selected == "Video Settings":
                self.draw_selected()
                self.game.draw_text("Sound Settings", 30, self.soundx, self.soundy)
                self.game.draw_text("Menu Colour Settings", 30, self.menucolourx, self.menucoloury)
            elif self.selected == "Sound Settings":
                self.game.draw_text("Video Settings", 30, self.videox, self.videoy)
                self.draw_selected()
                self.game.draw_text("Menu Colour Settings", 30, self.menucolourx, self.menucoloury)
            elif self.selected == "Menu Colour Settings":
                self.game.draw_text("Video Settings", 30, self.videox, self.videoy)
                self.game.draw_text("Sound Settings", 30, self.soundx, self.soundy)
                self.draw_selected()
            self.blit_menu()

    def move_selection(self):
        if self.game.DOWN_KEY:
            if self.state == "Options Video Settings":
                self.highlightedx, self.highlightedy = self.soundx, self.soundy
                self.selected = "Sound Settings"
                self.state = "Options Sound Settings"
            elif self.state == "Options Sound Settings":
                self.highlightedx, self.highlightedy = self.menucolourx, self.menucoloury
                self.selected = "Menu Colour Settings"
                self.state = "Options Menu Colour Settings"
            elif self.state == "Options Menu Colour Settings":
                self.highlightedx, self.highlightedy = self.videox, self.videoy
                self.selected = "Video Settings"
                self.state = "Options Video Settings"
        elif self.game.UP_KEY:
            if self.state == "Options Video Settings":
                self.highlightedx, self.highlightedy = self.menucolourx, self.menucoloury
                self.selected = "Menu Colour Settings"
                self.state = "Options Menu Colour Settings"
            elif self.state == "Options Menu Colour Settings":
                self.highlightedx, self.highlightedy = self.soundx, self.soundy
                self.selected = "Sound Settings"
                self.state = "Options Sound Settings"
            elif self.state == "Options Sound Settings":
                self.highlightedx, self.highlightedy = self.videox, self.videoy
                self.selected = "Video Settings"
                self.state = "Options Video Settings"
    
    def check_input(self):
        self.move_selection()
        if self.game.ENTER_KEY:
            if self.state == "Options Video Settings":
                self.game.current_menu = self.game.videosettings_menu
            elif self.state == "Options Sound Settings":
                pass
            elif self.state == "Options Menu Colour Settings":
                self.game.current_menu = self.game.coloursettings_menu

        elif self.game.ESCAPE_KEY:
            self.game.current_menu = self.game.main_menu
        
        self.run_menu_display = False

class MenuColourSettings(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.game = game
        self.state = "Menu Colour Settings"
        self.menucolourx, self.menucoloury = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.choice = 0
        self.menucolour_choice = None

    def display_menu(self):
        self.run_menu_display = True
        while self.run_menu_display:
            self.game.check_events()
            self.check_input()
            self.game.display_surface.fill(self.game.MENUCOLOUR)
            self.game.draw_text("Menu Colour Settings", 36, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 200)
            if self.choice == 0:
                self.game.draw_text("Menu Colour :", 30, self.menucolourx - 250, self.menucoloury + 40)
                self.game.draw_text(f"< Light Green-Blue {str(self.game.menucolours[self.choice])} >", 30, self.menucolourx + 130, self.menucoloury + 40)
            elif self.choice == 1:
                self.game.draw_text("Menu Colour :", 30, self.menucolourx - 250, self.menucoloury + 40)
                self.game.draw_text(f"< Light Orange {str(self.game.menucolours[self.choice])} >", 30, self.menucolourx + 130, self.menucoloury + 40)
            elif self.choice == 2:
                self.game.draw_text("Menu Colour :", 30, self.menucolourx - 250, self.menucoloury + 40)
                self.game.draw_text(f"< Light Purple {str(self.game.menucolours[self.choice])} >", 30, self.menucolourx + 130, self.menucoloury + 40)
            elif self.choice == 3:
                self.game.draw_text("Menu Colour :", 30, self.menucolourx - 250, self.menucoloury + 40)
                self.game.draw_text(f"< Black {str(self.game.menucolours[self.choice])} >", 30, self.menucolourx + 130, self.menucoloury + 40)
            self.blit_menu()
    
    def move_choice(self):
        if self.game.RIGHT_KEY:
            if -1 < self.choice < len(self.game.menucolours) - 1:
                self.choice += 1
            else:
                self.choice = len(self.game.menucolours) - 1
        elif self.game.LEFT_KEY:
            if 0 < self.choice < len(self.game.menucolours):
                self.choice -= 1
            else:
                self.choice = 0

    def check_input(self):
        self.move_choice()
        if self.game.ENTER_KEY:
            self.menucolour_choice = self.game.menucolours[self.choice]
            self.game.MENUCOLOUR = self.menucolour_choice
        elif self.game.ESCAPE_KEY:
            self.game.current_menu = self.game.options_menu
        self.run_menu_display = False

class VideoSettings(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.game = game
        self.state = "Video Settings Resolution"
        self.resolutionx, self.resolutiony = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.choice = 0
        self.resolution_choice = None
        #self.choice = f"<  {str(self.game.video_resolution[0][0])}x{str(self.game.video_resolution[0][1])}  >"

    def display_menu(self):
        self.run_menu_display = True
        while self.run_menu_display:
            self.game.check_events()
            self.check_input()
            self.game.display_surface.fill(self.game.MENUCOLOUR)
            self.game.draw_text("Video Settings", 36, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 200)
            if self.choice == 0:
                self.game.draw_text("Resolution :", 30, self.resolutionx - 120, self.resolutiony)
                self.game.draw_text(f"<  {str(self.game.video_resolution[self.choice][0])}x{str(self.game.video_resolution[self.choice][1])}  >", 30, self.resolutionx + 120, self.resolutiony)
            elif self.choice == 1:
                self.game.draw_text("Resolution :", 30, self.resolutionx - 120, self.resolutiony)
                self.game.draw_text(f"<  {str(self.game.video_resolution[self.choice][0])}x{str(self.game.video_resolution[self.choice][1])}  >", 30, self.resolutionx + 120, self.resolutiony)
            elif self.choice == 2:
                self.game.draw_text("Resolution :", 30, self.resolutionx - 120, self.resolutiony)
                self.game.draw_text(f"<  {str(self.game.video_resolution[self.choice][0])}x{str(self.game.video_resolution[self.choice][1])}  >", 30, self.resolutionx + 120, self.resolutiony)
            self.blit_menu()

    def move_choice(self):
        if self.game.RIGHT_KEY:
            if -1 < self.choice < len(self.game.video_resolution) - 1:
                self.choice += 1
            else:
                self.choice = len(self.game.video_resolution) - 1
        elif self.game.LEFT_KEY:
            if 0 < self.choice < len(self.game.video_resolution):
                self.choice -= 1
            else:
                self.choice = 0
    
    def check_input(self):
        self.move_choice()
        if self.game.ENTER_KEY:
            #self.game.choice = self.choice
            self.resolution_choice = self.game.video_resolution[self.choice]
            #self.game.change_resolution = True
            #self.game.running = False
            self.game.DISPLAY_W, self.game.DISPLAY_H = self.resolution_choice
            #self.game.DISPLAY_W, self.game.DISPLAY_H = self.resolution_choice
        elif self.game.ESCAPE_KEY:
            self.game.current_menu = self.game.options_menu
        self.run_menu_display = False

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Credits"
        self.creditsinfox, self.creditsinfoy = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
    
    def display_menu(self):
        self.run_menu_display = True
        while self.run_menu_display:
            self.game.check_events()
            self.check_input()
            self.game.display_surface.fill(self.game.MENUCOLOUR)
            self.game.draw_text("Credits", 36, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 200)
            self.game.draw_text("Made by Abj", 36, self.creditsinfox, self.creditsinfoy)
            self.game.draw_text("https://www.youtube.com/@CDcodes", 36, self.creditsinfox, self.creditsinfoy + 50)
            self.blit_menu()
    
    def check_input(self):
        if self.game.ESCAPE_KEY:
            self.game.current_menu = self.game.main_menu
        self.run_menu_display = False