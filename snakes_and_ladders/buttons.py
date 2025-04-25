import pygame

class Button:
    def __init__(self, button_image_path, pressed_button_image_path, position, scale = 1.0):
        self.button_image = pygame.image.load(button_image_path)
        self.pressed_button_image = pygame.image.load(pressed_button_image_path)

        original_width_button_image = self.button_image.get_width(); original_width_pressed_button_image = self.pressed_button_image.get_width()
        original_height_button_image = self.button_image.get_height(); original_height_pressed_button_image = self.pressed_button_image.get_height()
        scaled_width_button_image = int(original_width_button_image * scale); scaled_width_pressed_button_image = int(original_width_pressed_button_image * scale)
        scaled_height_button_image = int(original_height_button_image * scale); scaled_height_pressed_button_image = int(original_height_pressed_button_image * scale)

        self.image = pygame.transform.scale(self.button_image, (scaled_width_button_image, scaled_height_button_image))
        self.image_rect = self.image.get_rect(topleft = position)

        self.pressed_image = pygame.transform.scale(self.pressed_button_image, (scaled_width_pressed_button_image, scaled_height_pressed_button_image))
        self.pressed_image_rect = self.pressed_image.get_rect(topleft = position)

        self.pressed = False
        
        self.hover = False

    def draw(self, window):
        if not self.hover:
            window.blit(self.image, self.image_rect)
        else:
            window.blit(self.pressed_image, self.pressed_image_rect)

#ROLL_BUTTON = Button(os.path.join("assets", "roll_button.png"), os.path.join("assets", "roll_button_pressed.png"), (1110, 500), 0.3)
#if (self.image_rect.x, self.image_rect.y) < mouse_pos and 

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