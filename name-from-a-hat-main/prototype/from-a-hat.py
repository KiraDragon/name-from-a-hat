import pandas as pd
import random as rand
import tkinter as tk
import pygame
from tkinter import ttk
import time

pygame.mixer.init()

def destroy(popup):
    popup.destroy()

def play(filename):
    pygame.mixer.music.load("assets/" + filename + ".mp3")
    pygame.mixer.music.play(loops=0)

def popup(screensize, message, name, editedlst, title):
    top = tk.Toplevel(main)
    
    top.geometry(f'{screensize}+{200}+{200}')
    top.title(title)
    tk.Label(top, text=message).pack(anchor=tk.W)
    tk.Label(top, text=".").pack()
    tk.Label(top, text=".").pack()
    tk.Label(top, text=".").pack()
    tk.Label(top, text=name).pack()
    tk.Label(top, text = "-------------------------------------------------------------------").pack()
    tk.Label(top, text = "Congratulations to " + name + "! You won the lucky draw!").pack()
    tk.Label(top, text = "-------------------------------------------------------------------").pack()
    editedlst = list(filter((name).__ne__, editedlst))
    #add a button to continue if the list is long enoug
    again = ttk.Button(top, text="Pick Again", command=lambda : [pick_a_name(editedlst), destroy(top)])
    again.pack()
    
    play("win")
    time.sleep(2)
    play("cheer")

    return 0

def pick_a_name(lst):
    
    if len(lst) == 0:
        popup("500x200", "\t     There are no more names in the hat...\n\tThanks for using me!", "", [], "Empty Hat")
        return []
    else:
        filtered = lst
        #run program here
        pickedname = rand.choice(filtered)
        popup("1200x780", "  From " + str(len(filtered)) + " people, the name pulled out is: ", pickedname, filtered, "Name Picked")
        return filtered

def mainfunction(filename):
    filename = filename + ".xlsx"
    try:
        frame = pd.read_excel(filename)
        
    except Exception as e:
        popup("500x200", e, "", [], "File not found")
        return 0

    mainlst = frame.loc[:, "Name"].to_list()
    pick_a_name(mainlst)
    
    return 0

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

finally:
    main = tk.Tk()

    main.title("Pick a Name")
    window_width = 700
    window_height = 300

    screenwidth = main.winfo_screenwidth()
    screenheight = main.winfo_screenheight()

    centre_x = int(screenwidth/2 - window_width/2)
    centre_y = int(screenheight/2 - window_height/2)

    main.geometry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')

    label1 = ttk.Label(main, text="Pick a Name from the Hat", font=('Times', 18))
    label2 = ttk.Label(main, text="Enter the file name: ", font=("bold"))
    label3 = ttk.Label(main, text=".xlsx")
    filename = tk.StringVar()
    fileentry = ttk.Entry(main, textvariable=filename)
    
    label1.grid(row=0, column=1, padx=10, pady=20)
    label2.grid(row=1, column=1)
    label3.grid(row=1, column=3)
    fileentry.grid(row=1, column=2, padx=5)

    confirm = ttk.Button(main, text="Confirm", command=lambda : mainfunction(fileentry.get()))
    confirm.grid(row=5, column=2, padx=50, pady=50)

    main.mainloop()