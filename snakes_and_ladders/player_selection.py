import tkinter as tk, json, random, os, pygame
from tkinter import ttk

#file imports
#import engine

file_name = "game.json"
file_path = os.path.join("snakes_and_ladders", "game.json")

# PLAYER SELECTION

# each player with a different colour
# up to 4 players if needed
# button to proceed

CAT_RED = pygame.image.load(os.path.join("assets", "cat_red.png"))
CAT_YELLOW = pygame.image.load(os.path.join("assets", "cat_yellow.png"))
CAT_GREEN = pygame.image.load(os.path.join("assets", "cat_green.png"))
CAT_BLUE = pygame.image.load(os.path.join("assets", "cat_blue.png"))

DOG_RED = pygame.image.load(os.path.join("assets", "dog_red.png"))
DOG_YELLOW = pygame.image.load(os.path.join("assets", "dog_yellow.png"))
DOG_GREEN = pygame.image.load(os.path.join("assets", "dog_green.png"))
DOG_BLUE = pygame.image.load(os.path.join("assets", "dog_blue.png"))

SHEEP_RED = pygame.image.load(os.path.join("assets", "sheep_red.png"))
SHEEP_YELLOW = pygame.image.load(os.path.join("assets", "sheep_yellow.png"))
SHEEP_GREEN = pygame.image.load(os.path.join("assets", "sheep_green.png"))
SHEEP_BLUE = pygame.image.load(os.path.join("assets", "sheep_blue.png"))

FLY_RED = pygame.image.load(os.path.join("assets", "fly_red.png"))
FLY_YELLOW = pygame.image.load(os.path.join("assets", "fly_yellow.png"))
FLY_GREEN = pygame.image.load(os.path.join("assets", "fly_green.png"))
FLY_BLUE = pygame.image.load(os.path.join("assets", "fly_blue.png"))

def start_button_func():
    total_players = 0
    player_names_colour = {}
    player_indicator = {}

    player_1_name = player_1_entry_var.get(); player_2_name = player_2_entry_var.get(); player_3_name = player_3_entry_var.get(); player_4_name = player_4_entry_var.get()

    if player_1_name != "":
        player_1_colour = player_1_radiobutton_var.get()
        if player_1_colour == "":
            player_1_colour = random.choice(["red", "green", "yellow", "blue"])

        total_players += 1
        if player_1_colour == "red":
            player_names_colour["cat"] = [player_1_name, player_1_colour]
        elif player_1_colour == "yellow":
            player_names_colour["cat"] = [player_1_name, player_1_colour]
        elif player_1_colour == "green":
            player_names_colour["cat"] = [player_1_name, player_1_colour]
        elif player_1_colour == "blue":
            player_names_colour["cat"] = [player_1_name, player_1_colour]

    if player_2_name != "":
        player_2_colour = player_2_radiobutton_var.get()
        if player_2_colour == "":
            player_2_colour = random.choice(["red", "green", "yellow", "blue"])

        total_players += 1
        if player_2_colour == "red":
            player_names_colour["dog"] = [player_2_name, player_2_colour]
        elif player_2_colour == "yellow":
            player_names_colour["dog"] = [player_2_name, player_2_colour]
        elif player_2_colour == "green":
            player_names_colour["dog"] = [player_2_name, player_2_colour]
        elif player_2_colour == "blue":
            player_names_colour["dog"] = [player_2_name, player_2_colour]

    if player_3_name != "":
        player_3_colour = player_3_radiobutton_var.get()
        if player_3_colour == "":
            player_3_colour = random.choice(["red", "green", "yellow", "blue"])
        
        total_players += 1
        if player_3_colour == "red":
            player_names_colour["sheep"] = [player_3_name, player_3_colour]
        elif player_3_colour == "yellow":
            player_names_colour["sheep"] = [player_3_name, player_3_colour]
        elif player_3_colour == "green":
            player_names_colour["sheep"] = [player_3_name, player_3_colour]
        elif player_3_colour == "blue":
            player_names_colour["sheep"] = [player_3_name, player_3_colour]

    if player_4_name != "":
        player_4_colour = player_4_radiobutton_var.get()
        if player_4_colour == "":
            player_4_colour = random.choice(["red", "green", "yellow", "blue"])

        total_players += 1
        if player_4_colour == "red":
            player_names_colour["fly"] = [player_4_name, player_4_colour]
        elif player_4_colour == "yellow":
            player_names_colour["fly"] = [player_4_name, player_4_colour]
        elif player_4_colour == "green":
            player_names_colour["fly"] = [player_4_name, player_4_colour]
        elif player_4_colour == "blue":
            player_names_colour["fly"] = [player_4_name, player_4_colour]
    
    player_indicator["Positions"] = {key: 0 for key, value in player_names_colour.items()}
    player_indicator["Turns"] = {key: False for key, value in player_names_colour.items()}
    player_indicator["Rects"] = {key: {"x": random.randrange(20, 80, 20), "y": random.randrange(520, 1000, 20)} for key, value in player_names_colour.items()}

    if total_players != 0:
        PLAYER_SELECTION.destroy()
        json_file_handler(total_players, player_names_colour, player_indicator)

def json_file_handler(total_players, player_names_colour, player_indicator):
    print(f"Creating a new file called: {file_name}\n")
    template = {"Settings": {"Players": player_names_colour, "Total_players": total_players}, "Game": {"Players": player_indicator}}
            
    if os.path.exists(file_name):
        with open(file_name, "w") as file:
            print(f"\nFile name: '{file_name}' has been resetted successfully.")
            json.dump(template, file)
    else:
        with open(file_name, "x") as file:
            print(f"\nFile name: '{file_name}' has been created successfully.")
            json.dump(template, file)

PLAYER_SELECTION = tk.Tk()
PLAYER_SELECTION.title("Player selection!")

title_frm = ttk.Frame(PLAYER_SELECTION, padding= 10)
title_frm.grid()
title = ttk.Label(title_frm, text= "Choose a name and a colour!", font= "calibari 20",foreground= "dark blue").grid(column= 0, row= 0, padx= 50, pady= 30)

frm = ttk.Frame(PLAYER_SELECTION, padding= 10)
frm.grid()

player_1_entry_var = tk.StringVar()
player_1_radiobutton_var = tk.StringVar()
player_1_label = ttk.Label(frm, text= "Player 1 (Cat)", font= "Arial 14", foreground= "black").grid(column= 0, row= 0)
player_1_entry = ttk.Entry(frm, textvariable= player_1_entry_var,).grid(column= 0, row= 1, pady= 20, padx= 30)
player_1_radiobutton1 = ttk.Radiobutton(frm, value= "red", variable= player_1_radiobutton_var).grid(column=0, row=2, ipadx=30)
player_1_radiobutton1_colour = ttk.Label(frm, text="Red", foreground="red").grid(column= 0, row= 2)
player_1_radiobutton2 = ttk.Radiobutton(frm, value= "yellow", variable= player_1_radiobutton_var).grid(column=0, row=3, ipadx=30)
player_1_radiobutton2_colour = ttk.Label(frm, text="Yellow", foreground="goldenrod",).grid(column= 0, row= 3)
player_1_radiobutton3 = ttk.Radiobutton(frm,value= "green", variable= player_1_radiobutton_var).grid(column=0, row=4, ipadx=30)
player_1_radiobutton3_colour = ttk.Label(frm, text="Green", foreground="green").grid(column= 0, row= 4)
player_1_radiobutton4 = ttk.Radiobutton(frm,value= "blue", variable= player_1_radiobutton_var).grid(column=0, row=5, ipadx=30)
player_1_radiobutton4_colour = ttk.Label(frm, text="Blue", foreground="blue").grid(column= 0, row= 5)

player_2_entry_var = tk.StringVar()
player_2_radiobutton_var = tk.StringVar()
player_2_label = ttk.Label(frm, text= "Player 2 (Dog)", font= "Arial 14", foreground= "black").grid(column= 1, row= 0)
player_2_entry = ttk.Entry(frm, textvariable= player_2_entry_var).grid(column= 1, row= 1, pady= 20, padx= 30)
player_2_radiobutton1 = ttk.Radiobutton(frm, value= "red", variable= player_2_radiobutton_var).grid(column=1, row=2, ipadx=30)
player_2_radiobutton1_colour = ttk.Label(frm, text="Red", foreground="red").grid(column= 1, row= 2)
player_2_radiobutton2 = ttk.Radiobutton(frm, value= "yellow", variable= player_2_radiobutton_var).grid(column=1, row=3, ipadx=30)
player_2_radiobutton2_colour = ttk.Label(frm, text="Yellow", foreground="goldenrod",).grid(column= 1, row= 3)
player_2_radiobutton3 = ttk.Radiobutton(frm,value= "green", variable= player_2_radiobutton_var).grid(column=1, row=4, ipadx=30)
player_2_radiobutton3_colour = ttk.Label(frm, text="Green", foreground="green").grid(column= 1, row= 4)
player_2_radiobutton4 = ttk.Radiobutton(frm,value= "blue", variable= player_2_radiobutton_var).grid(column=1, row=5, ipadx=30)
player_2_radiobutton4_colour = ttk.Label(frm, text="Blue", foreground="blue").grid(column= 1, row= 5)

player_3_entry_var = tk.StringVar()
player_3_radiobutton_var = tk.StringVar()
player_3_label = ttk.Label(frm, text= "Player 3 (Sheep)", font= "Arial 14", foreground= "black").grid(column= 2, row= 0)
player_3_entry = ttk.Entry(frm, textvariable= player_3_entry_var).grid(column= 2, row= 1, pady= 20, padx= 30)
player_3_radiobutton1 = ttk.Radiobutton(frm, value= "red", variable= player_3_radiobutton_var).grid(column=2, row=2, ipadx=30)
player_3_radiobutton1_colour = ttk.Label(frm, text="Red", foreground="red").grid(column= 2, row= 2)
player_3_radiobutton2 = ttk.Radiobutton(frm, value= "yellow", variable= player_3_radiobutton_var).grid(column=2, row=3, ipadx=30)
player_3_radiobutton2_colour = ttk.Label(frm, text="Yellow", foreground="goldenrod",).grid(column= 2, row= 3)
player_3_radiobutton3 = ttk.Radiobutton(frm,value= "green", variable= player_3_radiobutton_var).grid(column=2, row=4, ipadx=30)
player_3_radiobutton3_colour = ttk.Label(frm, text="Green", foreground="green").grid(column= 2, row= 4)
player_3_radiobutton4 = ttk.Radiobutton(frm,value= "blue", variable= player_3_radiobutton_var).grid(column=2, row=5, ipadx=30)
player_3_radiobutton4_colour = ttk.Label(frm, text="Blue", foreground="blue").grid(column= 2, row= 5)

player_4_entry_var = tk.StringVar()
player_4_radiobutton_var = tk.StringVar()
player_4_label = ttk.Label(frm, text= "Player 4 (Fly)", font= "Arial 14", foreground= "black").grid(column= 3, row= 0)
player_4_entry = ttk.Entry(frm, textvariable= player_4_entry_var).grid(column= 3, row= 1, pady= 20, padx= 30)
player_4_radiobutton1 = ttk.Radiobutton(frm, value= "red", variable= player_4_radiobutton_var).grid(column=3, row=2, ipadx=30)
player_4_radiobutton1_colour = ttk.Label(frm, text="Red", foreground="red").grid(column= 3, row= 2)
player_4_radiobutton2 = ttk.Radiobutton(frm, value= "yellow", variable= player_4_radiobutton_var).grid(column=3, row=3, ipadx=30)
player_4_radiobutton2_colour = ttk.Label(frm, text="Yellow", foreground="goldenrod",).grid(column= 3, row= 3)
player_4_radiobutton3 = ttk.Radiobutton(frm,value= "green", variable= player_4_radiobutton_var).grid(column=3, row=4, ipadx=30)
player_4_radiobutton3_colour = ttk.Label(frm, text="Green", foreground="green").grid(column= 3, row= 4)
player_4_radiobutton4 = ttk.Radiobutton(frm,value= "blue", variable= player_4_radiobutton_var).grid(column=3, row=5, ipadx=30)
player_4_radiobutton4_colour = ttk.Label(frm, text="Blue", foreground="blue").grid(column= 3, row= 5)

start_button_frm = ttk.Frame(PLAYER_SELECTION, padding= 10)
start_button_frm.grid()
start_button = ttk.Button(start_button_frm, text= "START!", padding= 10, command= start_button_func).grid(column= 0, row= 0, pady= 20)

splitter1 = ttk.Separator(PLAYER_SELECTION, orient= "horizontal")
splitter1.place(relx= 0, rely= 0.275, relheight= 0, relwidth=1,)
splitter2 = ttk.Separator(PLAYER_SELECTION, orient= "vertical")
splitter2.place(relx= 0.255, rely= 0.275, relheight=0.51 , relwidth=0)
splitter3 = ttk.Separator(PLAYER_SELECTION, orient= "vertical")
splitter3.place(relx= 0.5, rely= 0.275, relheight=0.51 , relwidth=0)
splitter4 = ttk.Separator(PLAYER_SELECTION, orient= "vertical")
splitter4.place(relx= 0.755, rely= 0.275, relheight=0.51 , relwidth=0)
splitter5 = ttk.Separator(PLAYER_SELECTION, orient= "horizontal")
splitter5.place(relx= 0, rely= 0.786, relheight= 0, relwidth=1,)

PLAYER_SELECTION.mainloop()