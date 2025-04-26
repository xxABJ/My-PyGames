import pygame, os, json, sys

# gameclass

# make a menu class that generates a menu on the pygame window.
# make a button class that generates buttons on the menu/other.
# make a game class? (prob have to draw the actual game.. maybe)

def load_settings():
    with open("game.json", "r") as file:
        return json.load(file)
    
def save_settings(json_variable):
        with open("game.json", "w") as file:
            json.dump(json, file)

def json_turn_handler(turns, json_variable, Total_players):
    reset = True
    turn = 0

    while reset:
        for key, value in turns.items():
            if value == True:
                turn += 1
        if turn == Total_players:
            reset = False
        else:
            return
        
    json_reset_turns(turns, json_variable)

def json_reset_turns(turns, json_variable):
    for key, value in turns.items():
        if value == True:
            turns[key] = False
            save_settings(json_variable)

class MENU():
    def __init__(self, pygame_window, button_list):
        self.pygame_window = pygame_window
        self.button_list = button_list

class Button(MENU):
    def __init__(self, button_image_path, hover_button_image_path, pressed_button_image_path, position, scale        = 1.0):
        json_file = load_settings()

        self.button_image = pygame.image.load(button_image_path)
        self.hover_button_image_path = pygame.image.load(hover_button_image_path)
        self.pressed_button_image = pygame.image.load(pressed_button_image_path)

        original_width_button_image = self.button_image.get_width(); original_height_button_image = self.button_image.get_height()
        original_width_hover_button_image_path = self.hover_button_image_path.get_width(); original_height_hover_button_image_path = self.hover_button_image_path.get_height()
        original_width_pressed_button_image = self.pressed_button_image.get_width(); original_height_pressed_button_image = self.pressed_button_image.get_height()
        
        scaled_width_button_image = int(original_width_button_image * scale); scaled_height_button_image = int(original_height_button_image * scale)
        scaled_width_hover_button_image_path = int(original_width_hover_button_image_path * scale); scaled_height_hover_button_image_path = int(original_height_hover_button_image_path * scale)
        scaled_width_pressed_button_image = int(original_width_pressed_button_image * scale); scaled_height_pressed_button_image = int(original_height_pressed_button_image * scale)

        self.image = pygame.transform.scale(self.button_image, (scaled_width_hover_button_image_path, scaled_height_hover_button_image_path))
        self.image_rect = self.image.get_rect(topleft = position)

        self.hover_image = pygame.transform.scale(self.hover_button_image_path, (scaled_width_button_image, scaled_height_button_image))
        self.hover_image_rect = self.image.get_rect(topleft = position)

        self.pressed_image = pygame.transform.scale(self.pressed_button_image, (scaled_width_pressed_button_image, scaled_height_pressed_button_image))
        self.pressed_image_rect = self.pressed_image.get_rect(topleft = position)

        self.pressed = False

        self.hover = False

    def draw(self, window):
        if not self.hover:
            window.blit(self.image, self.image_rect)
        else:
            window.blit(self.hover_image, self.hover_image_rect)

        if not self.pressed:
            window.blit(self.image, self.image_rect)
        else:
            window.blit(self.pressed_image, self.pressed_image_rect)

    def is_over_button(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_hover = mouse_pos[0] in range(self.image_rect.x, self.image_rect.x + self.image_rect.width) and mouse_pos[1] in range(self.image_rect.y, self.image_rect.y + self.image_rect.height)

        if mouse_hover:
            self.hover = True
            return True

        if not mouse_hover:
            self.hover = False

        return False

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.image_rect.collidepoint(mouse_pos):
            if mouse_pressed and not self.pressed:
                self.pressed = True
                return True

        if not mouse_pressed:
            self.pressed = False

        return False