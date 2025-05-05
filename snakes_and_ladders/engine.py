import pygame, os, sys, json, random

#Files
import player_selection, dice, board
from buttons import Button

# SNAKES AND LADDERS

# maximum four players
# each player has a colour
# dice should be rolled with each players turn
# board functions include going up the ladder and down the snake
# add gameplay audio

def load_settings():
    with open("game.json", "r") as file:
        return json.load(file)
    
def save_settings(game):
    with open("game.json", "w") as file:
        json.dump(game, file)

WIDTH, HEIGHT = board.BLOCKSIZE * board.BLOCKCOUNT, board.BLOCKSIZE * board.BLOCKCOUNT - (board.BLOCKSIZE - board.TOP_BOTTOM_EXTRA)*2
#WIDTH, HEIGHT = 1200, 1040

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and ladders !")

ROLL_BUTTON = Button(os.path.join("assets", "roll_button.png"), os.path.join("assets", "roll_button_hover.png"), os.path.join("assets", "roll_button_pressed.png"), (1110, 500), 0.3)
RED_BUTTON = Button(os.path.join("assets", "red_button.png"), os.path.join("assets", "red_button_hover.png"), os.path.join("assets", "red_button_pressed.png"), (1110, 550), 2)

#globals
cat = "cat"
dog = "dog"
sheep = "sheep"
fly = "fly"

def sprite_assigner(key, value):
    if key == "cat":
        global cat
        if value[1] == "red":
            cat = player_selection.CAT_RED
        elif value[1] == "yellow":
            cat = player_selection.CAT_YELLOW
        elif value[1] == "green":
            cat = player_selection.CAT_GREEN
        elif value[1] == "blue":
            cat = player_selection.CAT_BLUE

    elif key == "dog":
        global dog
        if value[1] == "red":
            dog = player_selection.DOG_RED
        elif value[1] == "yellow":
            dog = player_selection.DOG_YELLOW
        elif value[1] == "green":
            dog = player_selection.DOG_GREEN
        elif value[1] == "blue":
            dog = player_selection.DOG_BLUE

    elif key == "sheep":
        global sheep
        if value[1] == "red":
            sheep = player_selection.SHEEP_RED
        elif value[1] == "yellow":
            sheep = player_selection.SHEEP_YELLOW
        elif value[1] == "green":
            sheep = player_selection.SHEEP_GREEN
        elif value[1] == "blue":
            sheep = player_selection.SHEEP_BLUE
    
    elif key == "fly":
        global fly
        if value[1] == "red":
            fly = player_selection.FLY_RED
        elif value[1] == "yellow":
            fly = player_selection.FLY_YELLOW
        elif value[1] == "green":
            fly = player_selection.FLY_GREEN
        elif value[1] == "blue":
            fly = player_selection.FLY_BLUE

def idling(dictionary):
    for key, value in dictionary.items():
        value[1][0] += random.randrange(0, 2, 1)
        value[1][1] += random.randrange(0, 2, 1)
        value[1][0] -= random.randrange(0, 2, 1)
        value[1][1] -= random.randrange(0, 2, 1)
        #pygame.time.delay(random.randrange(20, 30, 2))
    return dictionary

def draw(game, player_rects, cat, dog, sheep, fly):

    #window
    WINDOW.blit(board.BOARD, (0,0))
    ROLL_BUTTON.draw(WINDOW)
    RED_BUTTON.draw(WINDOW)
    
    #players
    if cat != "cat":
        cat_rect = player_rects["cat"][1]
        WINDOW.blit(cat, cat_rect)
    if dog != "dog":
        dog_rect = player_rects["dog"][1]
        WINDOW.blit(dog, dog_rect)
    if sheep != "sheep":
        sheep_rect = player_rects["sheep"][1]
        WINDOW.blit(sheep, sheep_rect)
    if fly != "fly":
        fly_rect = player_rects["fly"][1]
        WINDOW.blit(fly, fly_rect)

    #blocks
    pygame.display.update()

def main():
    game = load_settings()

    player_types = game["Settings"]["Players"]
    player_rects = {}
    for key, value in player_types.items():
        sprite_assigner(key, value)

    run = True
    clock = pygame.time.Clock()
    pygame.init()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if ROLL_BUTTON.is_pressed(): 
            print("\nRoll button is pressed !")
            dice.dice()
        elif ROLL_BUTTON.is_over_button():
            pass
            #print("\nMouse is over the roll button !")
        
        if RED_BUTTON.is_pressed():
            print("\nRed button is pressed !")
        elif RED_BUTTON.is_over_button():
            pass

        board.player_rect_generator(game, player_rects)
        idling(player_rects)
        draw(game, player_rects, cat, dog, sheep, fly)
        #dice.dice()

        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()