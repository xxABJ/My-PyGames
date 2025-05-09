import tkinter as tk, json, random
from tkinter import ttk

# DICE

# should have it's own window with every play,
# state which charater's turn is and how much the result is
# maybe some dice audio

def load_settings():
    with open("game.json", "r") as file:
        return json.load(file)
    
def save_settings(game):
        with open("game.json", "w") as file:
            json.dump(game, file)

def turn_handler(turns, file, Total_players):
    reset = True
    turn = 0

    while reset:
        for key, value in turns.items():
            if value == True:
                turn += 1
        if turn == Total_players:
            reset = False
        else:
            return
        
    reset_turns(turns, file)

def reset_turns(turns, file):
    for key, value in turns.items():
        if value == True:
            turns[key] = False
            save_settings(file)

def random_numbers() -> int:
    return text_frame_var.set(random.randint(1,6))

def roll_dice_button_func():
    a = 0
    timer = 500
    while a < 50:
        DICE.after(timer, random_numbers)
        timer -= 5
        DICE.after(timer, random_numbers)
        timer -= 5
        a += 1
    roll_button.config(state= 'disabled')

def play_button_func():
    print(text_frame_var.get())
    text_frame_var.get()
    return DICE.destroy()

DICE = tk.Tk()
DICE.title("Roll the dice!")
#DICE.geometry()
frm = ttk.Frame(DICE, padding= 10)
frm.grid()

player_name_var = tk.StringVar()
player_label = ttk.Label(frm, textvariable= player_name_var, font= "IMPACT 20 bold", foreground= None, padding= 10)
player_label.grid(column= 0, row= 0, pady= 10, padx= 40)

text_frame_var = tk.IntVar(value= 0)
text_frame = ttk.Label(frm, textvariable= text_frame_var, font= "Arial 12 bold", foreground= "black")
text_frame.grid(column= 0, row= 1)

button_frm = ttk.Frame(DICE, padding= 40)
button_frm.grid()

roll_button = ttk.Button(button_frm, text= "ROLL!", command= roll_dice_button_func, padding= 5, state= 'active')
roll_button.grid(column=0, row= 0, pady= 10)

play_button = ttk.Button(button_frm, text= "PLAY!", command= play_button_func, padding= 5)
play_button.grid(column=1, row= 0, pady= 10)

#skip_button = ttk.Button(button_frm, text= "SKIP!", command= skip_button_func, padding= 5)
#skip_button.grid(column=2, row= 0, pady= 10)

#DICE.mainloop()

def dice():
    if player_name_var == "":
        return DICE.destroy
    player_settings = load_settings()

    Players = player_settings["Settings"]["Players"]
    total_players = player_settings["Settings"]["Total_players"]
    turns = player_settings["Game"]["Players"]["Turns"]

    turn_handler(turns, player_settings, total_players)

    for key, value in turns.items():
        if value == False:
            turns[key] = True

            player_name_var.set(Players[key][0])
            player_label.config(foreground= Players[key][1])
            save_settings(player_settings)
            break
    
    DICE.mainloop()
    

if __name__ == "__main__":
    dice()

