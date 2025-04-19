import tkinter as tk
from tkinter import ttk

#files
import ships
#from ships import *

#### TK WINDOW

def ship_side_and_colour():
    left_input = leftside_radiobutton_var.get(); right_input = rightside_radiobutton_var.get()
    if left_input and right_input:
        ROOT.destroy()
        return ships.draw_ships({"left": left_input, "right": right_input})              # using a func to extract ship configuration dictionary data

ROOT = tk.Tk()
ROOT.title("Configure your ships !")

frm = ttk.Frame(ROOT, padding= 10)
frm.grid() #grid

leftside_label = ttk.Label(frm, text= "Left ship!", font= "IMPACT 20", foreground= "cornflower blue").grid(column= 0, row= 0, padx=20)
rightside_label = ttk.Label(frm, text= "Right ship!", font= "IMPACT 20", foreground= "pale violet red").grid(column= 2, row= 0, padx=20)

leftside_instructions = ttk.Label(frm, text="Controls: W,D,S,A").grid(column=0,row=1)
rightside_instructions = ttk.Label(frm, text="Arrow keys: ^,>,v,<").grid(column=2, row=1)

#spacing
ttk.Label(frm, text= "").grid(column= 1, row= 2)

leftside_radiobutton_var = tk.StringVar()
leftside_radiobutton1 = ttk.Radiobutton(frm, value= "red", variable= leftside_radiobutton_var).grid(column=0, row=3, ipadx=30)
leftside_radiobutton1_colour = ttk.Label(frm, text="Red", foreground="red").grid(column= 0, row= 3)
leftside_radiobutton2 = ttk.Radiobutton(frm, value= "yellow", variable= leftside_radiobutton_var).grid(column=0, row=4, ipadx=30)
leftside_radiobutton2_colour = ttk.Label(frm, text="Yellow", foreground="goldenrod",).grid(column= 0, row= 4)
leftside_radiobutton3 = ttk.Radiobutton(frm,value= "green", variable= leftside_radiobutton_var).grid(column=0, row=5, ipadx=30)
leftside_radiobutton3_colour = ttk.Label(frm, text="Green", foreground="green").grid(column= 0, row= 5)
leftside_radiobutton4 = ttk.Radiobutton(frm,value= "blue", variable= leftside_radiobutton_var).grid(column=0, row=6, ipadx=30)
leftside_radiobutton4_colour = ttk.Label(frm, text="Blue", foreground="blue").grid(column= 0, row= 6)

rightside_radiobutton_var = tk.StringVar()
rightside_radiobutton1 = ttk.Radiobutton(frm, value= "red", variable= rightside_radiobutton_var).grid(column=2, row=3, ipadx=30)
rightside_radiobutton1_colour = ttk.Label(frm, text="Red", foreground="red").grid(column= 2, row= 3)
rightside_radiobutton2 = ttk.Radiobutton(frm, value= "yellow", variable= rightside_radiobutton_var).grid(column=2, row=4, ipadx=30)
rightside_radiobutton2_colour = ttk.Label(frm, text="Yellow", foreground="goldenrod",).grid(column= 2, row= 4)
rightside_radiobutton3 = ttk.Radiobutton(frm, value= "green", variable= rightside_radiobutton_var).grid(column=2, row=5, ipadx=30)
rightside_radiobutton3_colour = ttk.Label(frm, text="Green", foreground="green").grid(column= 2, row= 5)
rightside_radiobutton4 = ttk.Radiobutton(frm, value= "blue", variable= rightside_radiobutton_var).grid(column=2, row=6, ipadx=30)
rightside_radiobutton4_colour = ttk.Label(frm, text="Blue", foreground="blue").grid(column= 2, row= 6)

#spacing
ttk.Label(frm, text= "").grid(column= 1, row= 7)
ttk.Label(frm, text= "").grid(column= 1, row= 8)

button = ttk.Button(frm, text= "Start!", command= ship_side_and_colour, padding=5).grid(column= 1, row=9, pady=5)

splitter1 = ttk.Separator(ROOT, orient= "vertical")
splitter1.place(relx= 0.48, rely= 0, relheight= 0.75, relwidth=0)
splitter2 = ttk.Separator(ROOT, orient= "horizontal")
splitter2.place(relx= 0, rely= 0.75, relheight=0 , relwidth=1)

#ROOT.mainloop()