import pygame, os

#files
import game
#from game import *

### SHIPS

GREEN_SPACESHIP_LEFTSIDE = pygame.image.load(os.path.join("assets", "green_spaceship_leftside.png"))
GREEN_SPACESHIP_RIGHTSIDE = pygame.image.load(os.path.join("assets", "green_spaceship_rightside.png"))
BLUE_SPACESHIP_LEFTSIDE = pygame.image.load(os.path.join("assets", "blue_spaceship_leftside.png"))
BLUE_SPACESHIP_RIGHTSIDE = pygame.image.load(os.path.join("assets", "blue_spaceship_rightside.png"))
RED_SPACESHIP_LEFTSIDE = pygame.image.load(os.path.join("assets", "red_spaceship_leftside.png"))
RED_SPACESHIP_RIGHTSIDE = pygame.image.load(os.path.join("assets", "red_spaceship_rightside.png"))
YELLOW_SPACESHIP_LEFTSIDE = pygame.image.load(os.path.join("assets", "yellow_spaceship_leftside.png"))
YELLOW_SPACESHIP_RIGHTSIDE = pygame.image.load(os.path.join("assets", "yellow_spaceship_rightside.png"))

SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 80

RED_BULLET_COLOUR = (255, 0, 0)
GREEN_BULLET_COLOUR = (0, 255, 33)
YELLOW_BULLET_COLOUR = (255, 216, 0)
BLUE_BULLET_COLOUR = (0, 38, 255)

def draw_ships(ship_configuration_dictionary):                       # using a func to use extracted data for pygame

    leftship_rect = pygame.Rect(game.SPACESHIP_STARTPOINT_LEFTSIDE["x"], game.SPACESHIP_STARTPOINT_LEFTSIDE["y"], SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    leftship_colour = ship_configuration_dictionary["left"]
    leftship_sprite = None
    leftship_bulletcolour = None
    rightship_rect = pygame.Rect(game.SPACESHIP_STARTPOINT_RIGHTSIDE["x"], game.SPACESHIP_STARTPOINT_RIGHTSIDE["y"], SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    rightship_colour = ship_configuration_dictionary["right"]
    rightship_sprite = None
    rightship_bulletcolour = None

    if leftship_colour == 'red':
        leftship_sprite = RED_SPACESHIP_LEFTSIDE
        leftship_bulletcolour = [RED_BULLET_COLOUR, "Red"]
    elif leftship_colour == 'yellow':
        leftship_sprite = YELLOW_SPACESHIP_LEFTSIDE
        leftship_bulletcolour = [YELLOW_BULLET_COLOUR, "Yellow"]
    elif leftship_colour == 'green':
        leftship_sprite = GREEN_SPACESHIP_LEFTSIDE
        leftship_bulletcolour = [GREEN_BULLET_COLOUR, "Green"]
    elif leftship_colour == 'blue':
        leftship_sprite = BLUE_SPACESHIP_LEFTSIDE
        leftship_bulletcolour = [BLUE_BULLET_COLOUR, "Blue"]

    if rightship_colour == 'red':
        rightship_sprite= RED_SPACESHIP_RIGHTSIDE
        rightship_bulletcolour = [RED_BULLET_COLOUR, "Red"]
    elif rightship_colour == 'yellow':
        rightship_sprite = YELLOW_SPACESHIP_RIGHTSIDE
        rightship_bulletcolour = [YELLOW_BULLET_COLOUR, "Yellow"]
    elif rightship_colour == 'green':
        rightship_sprite = GREEN_SPACESHIP_RIGHTSIDE
        rightship_bulletcolour = [GREEN_BULLET_COLOUR, "Green"]
    elif rightship_colour == 'blue':
        rightship_sprite = BLUE_SPACESHIP_RIGHTSIDE
        rightship_bulletcolour = [BLUE_BULLET_COLOUR, "Blue"]

    leftship_sprite_rect_bulletcolour = [leftship_sprite, leftship_rect, leftship_bulletcolour]
    rightship_sprite_rect_bulletcolour = [rightship_sprite, rightship_rect, rightship_bulletcolour]

    return game.main(leftship_sprite_rect_bulletcolour, rightship_sprite_rect_bulletcolour)