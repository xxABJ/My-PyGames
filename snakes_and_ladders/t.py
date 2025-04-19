for block, players in player_block_info.items():
    
    for key, value in occupied_blocks.items():
        (x, y) = value
        print()
        print(f"value: {value}")
        
        if key[1] == 0 and key[1] not in draw_block_rects.keys():
            print("\nthe block is 0")
            draw_block_rects[key[0]] = (key[1], pygame.Rect(x, y, 20, 20)) 
        #break

        if block != 0:
            for corners, positions in block_premade_rects.items():
                draw_block_rects[block] = (corners, pygame.Rect(x + positions[0], y + positions[1], 20, 20))
                print(f"\nblock: {block} \nplayers: {players}")
            break
        else:
            pass

# CHANGE occupiedBlocks_playersOnBlocks_blockRects_playerBlockInfo, remove playersOnBlocks & so _blockrect are a dict that assigns {(playertype, corner), (the extra x&y)} , if playertype is on same block then when assigning corners, the duped player should have the OTHER correct corner of the same "BLOCK_HAS_"