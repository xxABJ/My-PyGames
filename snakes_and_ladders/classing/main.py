from game import Game

g = Game()
while g.running:
    g.current_menu.display_menu()
    #if not g.running and g.change_resolution:
        #g.DISPLAY_W, g.DISPLAY_H = g.video_resolution[g.choice]
        #g.running = True
        #continue
        #g.change_resolution = False
    g.game_loop()