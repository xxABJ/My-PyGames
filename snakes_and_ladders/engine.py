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

def draw(occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo, draw_block_rects):

    #window
    WINDOW.blit(board.BOARD, (0,0))

    #blocks
    draw_blocks(draw_block_rects)

    #players


    pygame.display.update()

def main():

    occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo = []
    draw_block_rects = {}

    run = True
    clock = pygame.time.Clock()
    pygame.init()

    game = load_settings()
    player_selection.PLAYER_SELECTION.mainloop()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        board.board(game)
        draw(occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo, draw_block_rects)
        #board.dice()

        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()