import pygame, os, sys, json

#Files
import player_selection, dice, board

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

def draw(game, player_rects):

    #window
    WINDOW.blit(board.BOARD, (0,0))
    
    #players
    cat_colour = game["Settings"]["Players"]["cat"][1]
    dog_colour = game["Settings"]["Players"]["dog"][1]
    sheep_colour = game["Settings"]["Players"]["sheep"][1]
    fly_colour = game["Settings"]["Players"]["fly"][1]
    
    if cat_colour == "red":
        WINDOW.blit(player_selection.CAT_RED, (550, 500))
    elif cat_colour == "yellow":
        WINDOW.blit(player_selection.CAT_YELLOW, (550, 500))
    elif cat_colour == "green":
        WINDOW.blit(player_selection.CAT_GREEN, (550, 500))
    elif cat_colour == "blue":
        WINDOW.blit(player_selection.CAT_RED, (550, 500))
    
    if dog_colour == "red":
        WINDOW.blit(player_selection.DOG_RED, (550, 500))
    elif dog_colour == "yellow":
        WINDOW.blit(player_selection.DOG_YELLOW, (550, 500))
    elif dog_colour == "green":
        WINDOW.blit(player_selection.DOG_GREEN, (550, 500))
    elif dog_colour == "blue":
        WINDOW.blit(player_selection.DOG_BLUE, (550, 500))
    
    if sheep_colour == "red":
        WINDOW.blit(player_selection.SHEEP_RED, (550, 500))
    elif sheep_colour == "yellow":
        WINDOW.blit(player_selection.SHEEP_YELLOW, (550, 500))
    elif sheep_colour == "green":
        WINDOW.blit(player_selection.SHEEP_GREEN, (550, 500))
    elif sheep_colour == "blue":
        WINDOW.blit(player_selection.SHEEP_BLUE, (550, 500))
    
    if fly_colour == "red":
        WINDOW.blit(player_selection.FLY_RED, (550, 500))
    elif fly_colour == "yellow":
        WINDOW.blit(player_selection.FLY_YELLOW, (550, 500))
    elif fly_colour == "green":
        WINDOW.blit(player_selection.FLY_GREEN, (550, 500))
    elif fly_colour == "blue":
        WINDOW.blit(player_selection.FLY_BLUE, (550, 500))

    #blocks
    pygame.display.update()

def main():
    game = load_settings()

    player_rects = {}

    run = True
    clock = pygame.time.Clock()
    pygame.init()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        board.player_rect_generator(game, player_rects)
        draw(game, player_rects)

        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()