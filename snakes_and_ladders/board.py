import pygame, os, random, json

# BOARD

# each block has it's own rect and mechanics
# simple and clear
# add audio with movement

def load_settings():
    with open("game.json", "r") as file:
        return json.load(file)

def save_settings(game):
        with open("game.json", "w") as file:
            json.dump(game, file)

BOARD = pygame.image.load(os.path.join("assets", "board", "snake_and_ladder_board.png"))

BLOCKSIZE = 100
BLOCKCOUNT = 12

TOP_BOTTOM_EXTRA = 20

BLOCKS = {
    "1": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "2": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "3": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "4": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "5": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA), 
    "6": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "7": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "8": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "9": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "10": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "11": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "12": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "13": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "14": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "15": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE), 
    "16": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "17": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "18": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "19": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "20": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "21": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "22": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "23": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "24": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "25": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE), 
    "26": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "27": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "28": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "29": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "30": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "31": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "32": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "33": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "34": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "35": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE), 
    "36": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "37": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "38": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "39": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "40": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "41": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "42": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "43": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "44": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "45": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE), 
    "46": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "47": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "48": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "49": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "50": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "51": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "52": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "53": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "54": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "55": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE), 
    "56": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "57": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "58": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "59": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "60": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "61": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "62": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "63": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "64": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "65": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE), 
    "66": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE), 
    "67": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "68": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "69": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "70": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "71": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "72": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "73": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "74": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "75": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "76": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE), 
    "77": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "78": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "79": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "80": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-9*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "81": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "82": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "83": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "84": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "85": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE), 
    "86": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "87": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "88": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "89": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "90": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE+TOP_BOTTOM_EXTRA-BLOCKSIZE),
    "91": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "92": (9*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "93": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "94": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "95": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA), 
    "96": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "97": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "98": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "99": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    "100": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE-BLOCKSIZE+TOP_BOTTOM_EXTRA),
    }

BLOCK_HAS_FOUR = {"tl": (round(BLOCKSIZE*0.25), round(BLOCKSIZE*0.25)), "tr": (round(BLOCKSIZE*0.75), round(BLOCKSIZE*0.25)), "bl": (round(BLOCKSIZE*0.25), round(BLOCKSIZE*0.75)), "br": (round(BLOCKSIZE*0.75), round(BLOCKSIZE*0.75))}

BLOCK_HAS_THREE = {"tl": (round(BLOCKSIZE*0.25), round(BLOCKSIZE*0.25)), "tr": (round(BLOCKSIZE*0.75), round(BLOCKSIZE*0.25)), "b": (round(BLOCKSIZE*0.6), round(BLOCKSIZE*0.5))}

BLOCK_HAS_TWO = {"l": (round(BLOCKSIZE*0.25), round(BLOCKSIZE*0.5)), "r": (round(BLOCKSIZE*0.75), round(BLOCKSIZE*0.5))}

BLOCK_HAS_ONE = {"m": (round(BLOCKSIZE*0.5), round(BLOCKSIZE*0.5))}

OCCUPIED_BLOCKS = {}

def block_elements(key, block_number, current_rects):
    ELEMENTS = {
    "2": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-4*BLOCKSIZE), #up to 23
    "13": (7*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE), #up to 93
    "16": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-2*BLOCKSIZE), #down to 4
    "26": (5*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE), #up to 45
    "38": (8*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-5*BLOCKSIZE), #down to 33
    "43": (3*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE), #up to 58
    "59": (2*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-6*BLOCKSIZE), #down to 42
    "62": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-10*BLOCKSIZE), #up to 84
    "73": (6*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-7*BLOCKSIZE), #down to 55
    "81": (1*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-11*BLOCKSIZE), #up to 100
    "91": (10*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-3*BLOCKSIZE), #down to 11
    "97": (4*BLOCKSIZE, BLOCKSIZE*BLOCKCOUNT-8*BLOCKSIZE), #down to 64
}
    
    if str(block_number) in ELEMENTS:
        translate = ELEMENTS[f"{block_number}"]
        print(f"\nChanging pos to: \n{translate}\n")
        return ELEMENTS[f"{block_number}"]
    return position(key, block_number, current_rects)

def position(key, block_number, current_rects):
    if block_number != 0:
        block = BLOCKS[f"{block_number}"]
        return block
    else:
        if key == 'cat':
            return (current_rects[key]["x"], current_rects[key]["y"])
        elif key == 'dog':
            return (current_rects[key]["x"], current_rects[key]["y"])
        elif key == 'sheep':
            return (current_rects[key]["x"], current_rects[key]["y"])
        elif key == 'fly':
            return (current_rects[key]["x"], current_rects[key]["y"])
        
def print_position(block_number): #print pos
    block = BLOCKS[f"{block_number}"]
    return print(f"\nCurrent position: \n{block}\n")

def position_indicators(file): # dict indicator of blocks
    current_positions = file["Game"]["Players"]["Positions"]
    current_rects = file["Game"]["Players"]["Rects"]
    for key, value in current_positions.items():
        OCCUPIED_BLOCKS[key, value] = block_elements(key, value, current_rects)
    return block_handler(OCCUPIED_BLOCKS)

def block_handler(OCCUPIED_BLOCKS):
    """Returns a list of dictionaries containing:\n
       Realtime occupied blocks with x & y positions,\n
       Total number of duplicated players,\n
       Draw block rects for pygame,\n
       The duplicated player block info."""
    
    temp = []
    playerBlockInfo = {}

    for key, value in OCCUPIED_BLOCKS.items():
        #print(key, value)
        for _ in OCCUPIED_BLOCKS:
            temp.append([key[1], value])
            break

    for key, value in OCCUPIED_BLOCKS.items():
        try:
            playerBlockInfo[key[1]] += 1
        except:
            playerBlockInfo[key[1]] = 1
    same_block = max(playerBlockInfo.values())
   
    print(f"\nplayerBlockInfo: {playerBlockInfo}")
    print(f"\nsame_block: {same_block}")
    print(f"\ntemp: {temp}")
    
    index_position = [] 
    if same_block == 1:
        occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo = [OCCUPIED_BLOCKS, 1, playerBlockInfo, BLOCK_HAS_ONE]

    elif same_block == 2:
        occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo = [OCCUPIED_BLOCKS, 2, playerBlockInfo]
        blocks = playerBlockInfo.keys()
        block_corner_dict = []
        
        for block in blocks:
            if playerBlockInfo[block] == 2:
                block_corner_dict.append({block: BLOCK_HAS_TWO})
        occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo.append([block_corner_dict, BLOCK_HAS_ONE])
    
    elif same_block == 3:
        occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo = [OCCUPIED_BLOCKS, 3, playerBlockInfo]
        blocks = playerBlockInfo.keys()
        block_corner_dict = []
        
        for block in blocks:
            if playerBlockInfo[block] == 3:
                block_corner_dict.append({block: BLOCK_HAS_THREE})
        occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo.append([block_corner_dict, BLOCK_HAS_ONE])

        for index, value in enumerate(temp):
            if value == temp[index-1]:
                index_position.append(index)
            elif value == temp[index-2]:
                index_position.append(index)

    elif same_block == 4:
        occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo = [OCCUPIED_BLOCKS, 4, playerBlockInfo, BLOCK_HAS_FOUR]

    print(f"\nindex_position: {index_position}")
    print("\noccupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo: ",occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo)
    print(f"\nOCCUPIED_BLOCKS: {OCCUPIED_BLOCKS}")

    return draw_blocks(draw_block_rects, occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo)
    #return occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo

def board(file):
    position_indicators(file)

    # func to take in specific rects

def draw_blocks(draw_block_rects, occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo):
    occupied_blocks = occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo[0]
    players_on_blocks = occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo[1]
    player_block_info = occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo[2] # set for extra info :p
    block_premade_rects = occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo[3]

    dynamic_index = 0
    saved_index = 0
    
    for key, value in occupied_blocks.items():
        (x, y) = value
        print("\n"+key[0], key[1])
        print(f"value: {value}")

        if key[1] == 0:
            print("the block is 0")
            draw_block_rects[key[0]] = (key[1], pygame.Rect(x, y, 20, 20))
            print(f"\ndraw_block_rects: {draw_block_rects}")

        else:
            if players_on_blocks == 2 or players_on_blocks == 3:
                indexes = []
                locate_sameblock = []

                for _ in range(len(block_premade_rects[0])):
                    indexes.append(_)
                for index in indexes:
                    locate_sameblock.append(list(block_premade_rects[0][index].keys())[0])
                print(f"indexes: {indexes}")

                locate_sameblock_dict = list(block_premade_rects[0][0].values())
                sameblock_corners = list(locate_sameblock_dict[0].keys())
                sameblock_positions = list(locate_sameblock_dict[0].values())
                corner = list(block_premade_rects[1].keys())
                position = list(block_premade_rects[1].values())

                print(f"locate_sameblock: {locate_sameblock}")
                print(f"locate_sameblock_dict[0]: {locate_sameblock_dict[0]}")
                print(f"sameblock_corners: {sameblock_corners}")
                print(f"corner: {corner}")
                print(f"sameblock_positions: {sameblock_positions}")
                print(f"positions: {position}")

                if key[1] in locate_sameblock:
                    draw_block_rects[key[0]] = (sameblock_corners[dynamic_index], pygame.Rect(x + sameblock_positions[dynamic_index][0], y + sameblock_positions[dynamic_index][1], 20, 20))
                    print(f"\ndraw_block_rects: {draw_block_rects}")
                    
                    print()
                    print(f"before method - dynamic_index: {dynamic_index}")

                    if dynamic_index < len(locate_sameblock)-1 and key[1] != locate_sameblock[0]:
                        dynamic_index =+ 1
                    elif len(locate_sameblock) == 1:
                        dynamic_index += 1
                    elif dynamic_index <= len(locate_sameblock)-1 and key[1] == locate_sameblock[0]:
                        dynamic_index = dynamic_index
                    else:
                        dynamic_index = 0
                    saved_index = dynamic_index

                    print()
                    print(f"after method - dynamic_index: {dynamic_index}")
                
                else:
                    dynamic_index = 0

                    draw_block_rects[key[0]] = (corner[dynamic_index], pygame.Rect(x + position[dynamic_index][0], y + position[dynamic_index][1], 20, 20))
                    print(f"\ndraw_block_rects: {draw_block_rects}")

                    dynamic_index = saved_index

            else:
                corners = list(block_premade_rects.keys())
                positions = list(block_premade_rects.values())

                print(f"corners: {corners}")
                print(f"positions: {positions}")

                draw_block_rects[key[0]] = (corners[dynamic_index], pygame.Rect(x + positions[dynamic_index][0], y + positions[dynamic_index][1], 20, 20))
                print(f"draw_block_rects: {draw_block_rects}")

                if len(corners)-1 == dynamic_index:
                    dynamic_index = 0
                elif len(corners)-1 > dynamic_index and len(corners) > 1:
                    dynamic_index += 1

    print()
    return draw_block_rects


game = load_settings()
#player_position = game["Game"]["Players"]["Positions"]["cat"]

#position(43)
#block_elements(43)
#position_indicators(game)
#block_handler()

if __name__ == "__main__":
    occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo = []
    draw_block_rects = {}
    
    board(game)

    #draw_blocks(draw_block_rects, occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo)
