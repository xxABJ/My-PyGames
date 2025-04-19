import pygame, sys, random, tkinter as tk
from pygame.math import Vector2
from tkinter import ttk

class SNAKE:
    def __init__(self):
        first_move = [Vector2(1,0), Vector2(-1,0), Vector2(0,1), Vector2(0,-1)]                         #this is so the update_head_graphics() can work ?
        self.body = [Vector2(start_x,start_y), Vector2(start_x,start_y), Vector2(start_x,start_y)]      #starting snake size (blocks)
        self.direction = random.choice(first_move)                                                      #snake direction
        self.color = (120,200,10)                                                                       #snake color  
        self.eat = False                                                                                #snake grow trigger
        #head
        self.head_up = pygame.image.load("assets/snake_head_up.png").convert_alpha()
        self.head_down = pygame.image.load("assets/snake_head_down.png").convert_alpha()
        self.head_right = pygame.image.load("assets/snake_head_right.png").convert_alpha()
        self.head_left = pygame.image.load("assets/snake_head_left.png").convert_alpha()
        #tail
        self.tail_up = pygame.image.load("assets/snake_tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("assets/snake_tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load("assets/snake_tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load("assets/snake_tail_left.png").convert_alpha()
        #body
        self.body_hotizontal = pygame.image.load("assets/snake_body_horizontal.png").convert_alpha()
        self.body_vertical = pygame.image.load("assets/snake_body_vertical.png").convert_alpha()
        #corner
        self.corner_tr = pygame.image.load("assets/snake_corner_tr.png").convert_alpha()
        self.corner_tl = pygame.image.load("assets/snake_corner_tl.png").convert_alpha()
        self.corner_br = pygame.image.load("assets/snake_corner_br.png").convert_alpha()
        self.corner_bl = pygame.image.load("assets/snake_corner_bl.png").convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):                           #grid position locator
            x_pos = int(block.x * cell_size)                                #x axis
            y_pos = int(block.y * cell_size)                                #y axis
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)    #rect outlining

            if index == 0:
                ds.blit(self.head, snake_rect)
            elif index == len(self.body) - 1:
                ds.blit(self.tail, snake_rect)

            else:
                previous_block = self.body[index + 1]
                next_block = self.body[index - 1]

                if previous_block - next_block == Vector2(2,0) or previous_block - next_block == Vector2(-2,0):
                    ds.blit(self.body_hotizontal, snake_rect)
                elif previous_block - next_block == Vector2(0,2) or previous_block - next_block == Vector2(0,-2):
                    ds.blit(self.body_vertical, snake_rect)

                else:
                    corner_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
                    if block - next_block == Vector2(-1,0) and block - previous_block == Vector2(0,-1) or block - next_block == Vector2(0,-1) and block - previous_block == Vector2(-1,0): # TR
                        ds.blit(self.corner_tr, corner_rect)
                    if block - next_block == Vector2(1,0) and block - previous_block == Vector2(0,-1) or block - next_block == Vector2(0,-1) and block - previous_block == Vector2(1,0): # TL
                        ds.blit(self.corner_tl, corner_rect)
                    if block - next_block == Vector2(-1,0) and block - previous_block == Vector2(0,1) or block - next_block == Vector2(0,1) and block - previous_block == Vector2(-1,0): # BR
                        ds.blit(self.corner_br, corner_rect)
                    if block - next_block == Vector2(1,0) and block - previous_block == Vector2(0,1) or block - next_block == Vector2(0,1) and block - previous_block == Vector2(1,0): # BL
                        ds.blit(self.corner_bl, corner_rect)

    def update_head_graphics(self):
        head_direction = self.body[0] - self.body[1]
        if head_direction == Vector2(0,-1): self.head = self.head_up
        elif head_direction == Vector2(0,1): self.head = self.head_down
        elif head_direction == Vector2(1,0): self.head = self.head_right
        elif head_direction == Vector2(-1,0): self.head = self.head_left

    def update_tail_graphics(self):
        tail_direction = self.body[-1] - self.body[-2]
        if tail_direction == Vector2(0,1): self.tail = self.tail_up
        elif tail_direction == Vector2(0,-1): self.tail = self.tail_down
        elif tail_direction == Vector2(-1,0): self.tail = self.tail_right
        elif tail_direction == Vector2(1,0): self.tail = self.tail_left      

    def move_snake(self):
        if self.eat == False:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
        else:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.eat = False
            global total_score
            total_score += 1

    #def draw_checkers():
    
class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        #pygame.draw.rect(ds, (self.color), fruit_rect)
        ds.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1) #grid x_axis
        self.y = random.randint(0, cell_number - 1) #grid y_axis
        self.pos = Vector2(self.x, self.y)          #grid outline
        self.color = (200,10,10)                    #fruit color

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.fail = False

    def update(self):
        self.snake.move_snake()
        self.check_eat()
        if game_start == True: #Checks for an indicator related to a reset system.
            self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_eat(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.eat = True

    def check_fail(self):
        if not 0 <= self.snake.body[0].x <= cell_number-1 or not 0 <= self.snake.body[0].y <= cell_number-1:
            self.fail = True

        if self.snake.body[0] in self.snake.body[1:]:
            self.fail = True
            
        if self.fail == True:
            fail_window()
            global game_start
            game_start = False
    
def fail_window():
    window = tk.Tk()
    window.geometry("300x180")
    window.title("OOPS")
    title = ttk.Label(window, text= "YOU HAVE CRASHED!", font= ("Calibri", 24, 'bold'), foreground= 'red')
    title.pack(pady= 5)
    text = ttk.Label(window, text = f'Your total score is: {total_score} !', font= ("Calibri", 18, 'bold'))
    text.pack(pady= 15)
    button = ttk.Button(window, text = 'Press "R" to restart !', command = lambda: print("Exit the window first :p"))
    button.pack(pady = 10)
    window.mainloop()

pygame.init()
cell_size = 40
cell_number = 20
start_x = random.randint(1, cell_number - 2)
start_y = random.randint(1, cell_number - 2)
ds = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number)) #800x800
clock = pygame.time.Clock()
apple = pygame.image.load("assets/apple.png").convert_alpha()

main_game = MAIN()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
game_start = False
disable_keys = False
total_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            if main_game.fail == True:
                game_start = False
            else:
                main_game.update()

        if event.type == pygame.KEYDOWN:    
            if disable_keys == False:
                main_game.fail = False
                #"Start" the game with the arrow keys
                if event.key == pygame.K_UP:
                    game_start = True
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0,-1)
                        break
                if event.key == pygame.K_RIGHT:
                    game_start = True
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1,0)
                        break
                if event.key == pygame.K_DOWN:
                    game_start = True
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0,1)
                        break
                if event.key == pygame.K_LEFT:
                    game_start = True
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1,0)
                        break
            #Reset the game after pressing the r button
            if event.key == pygame.K_r:
                if main_game.fail == True and game_start == False:
                    main_game = MAIN()

    #"Start" and Reset system
    if game_start == False:
        if main_game.fail == True:
            disable_keys = True
        else: #"Start" after a reset.
            disable_keys = False
            ds.fill((25,55,25))
    else:
        ds.fill((25,55,25))
        main_game.draw_elements()
    
    pygame.display.update()
    clock.tick(60)