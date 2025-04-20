corner_index = 0
position_index = 0
for block, players in player_block_info.items():
    print(f"\nblock: {block}")

    for key, value in occupied_blocks.items():
        print(f"top corner_index: {corner_index}")
        print(f"top position_index: {position_index}")
        (x, y) = value
        print(key[0], key[1])
        print(f"value: {value}")

        if key[1] == 0: #and key[1] not in draw_block_rects.keys():
            print("the block is 0")
            draw_block_rects[key[0]] = (key[1], pygame.Rect(x, y, 20, 20)) 
            break  

        else:#if key[1] != 0: #and block not in draw_block_rects.keys():
            
            corners = list(block_premade_rects.keys())
            positions = list(block_premade_rects.values())

            if len(corners)-1 == corner_index:
                corner_index = 0
                position_index = 0
            elif len(corners)-1 > corner_index and len(corners) > 1:
                corner_index += 1
                position_index += 1

            print(f"bottom corner_index: {corner_index}")
            print(f"bottom position_index: {position_index}")

            print(f"corners: {corners}")
            print(f"positions: {positions}")
        
            draw_block_rects[block] = (corners[corner_index], pygame.Rect(x + positions[position_index][0], y + positions[position_index][1], 20, 20))
            #position_index += 1

            print(f"block: {block} \nplayers: {players}")
            print(draw_block_rects[block], "\n")

            #for corners, positions in block_premade_rects.items():
            #    draw_block_rects[block] = (corners, pygame.Rect(x + positions[0], y + positions[1], 20, 20))
            #    print(f"\nblock: {block} \nplayers: {players}")
            #    print(draw_block_rects[block])
            
            #if len(corners)-1 > corner_index and len(corners) > 1:
            #    corner_index += 1
            #    position_index += 1



# CHANGE occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo, remove playersOnBlocks & so _blockrect are a dict that assigns {(playertype, corner), (the extra x&y)} , if playertype is on same block then when assigning corners, the duped player should have the OTHER correct corner of the same "BLOCK_HAS_"