import pandas as pd
import random as rand
import tkinter as tk
import pygame
from tkinter import ttk

pygame.mixer.init()

def destroy(popup):
    popup.destroy()

def play(filename):
    pygame.mixer.music.load("assets/" + filename + ".mp3")
    pygame.mixer.music.play(loops=0)

def popup(screensize, message, name, editedlst, title):
    top = tk.Toplevel(main)
    
    top.iconbitmap("assets/pshico.ico")

    top.geometry(f'{screensize}+{800}+{250}')
    top.configure(bg='#012456')
    top.title(title)

    #tk.Label(top, bg='#012456', fg='#000', text="\nLucky Draw Results:\n", font=('Terminal', 20)).pack(anchor=tk.W)

    tk.Label(top, bg='#012456', fg='#fff', text= "\n>" + message, font=('Terminal', 14)).pack(anchor=tk.W)
    tk.Label(top, bg='#012456', fg='#fff', text = ".", font=('Terminal', 14)).pack()
    tk.Label(top, bg='#012456', fg='#fff', text = ".", font=('Terminal', 14)).pack()
    tk.Label(top, bg='#012456', fg='#fff', text = ".", font=('Terminal', 14)).pack()
    tk.Label(top, bg='#012456', fg='#fff', text = ".", font=('Terminal', 14)).pack()
    tk.Label(top, bg='#012456', fg='#fff', text = "-------------------------------------------------------------------", font=('Terminal', 12, 'bold')).pack()
    changinglabel = tk.Label(top, bg='#012456', fg='#fff', text="3", font=('BankGothic Lt BT', 24))

    play("beep")

    def on_after():
        changinglabel.configure( text="2")
        play("beep")

    def on_after2():
        changinglabel.configure( text="1")
        play("beep")

    def on_after3():
        changinglabel.configure( text=name)
        play("cheer")

    def addwinner():
        winner = tk.Label(top, bg='#012456', fg='#fff', text="\nCongratulations to " + name + "!\n You won the lucky draw!\n", font=('Terminal', 14, 'bold'))

        winner.pack()
        
    changinglabel.pack()
    changinglabel.after(1500, on_after)
    changinglabel.after(3000, on_after2)
    changinglabel.after(4500, on_after3)
    top.after(6000, addwinner)

    tk.Label(top, bg='#012456', fg='#fff', text = "-------------------------------------------------------------------", font=('Terminal', 14, 'bold')).pack()
    
    editedlst = list(filter((name).__ne__, editedlst))
    #add a button to continue if the list is long enough
    again = ttk.Button(top, text="Pick Again", command=lambda : [pick_a_name(editedlst), destroy(top)])
    again.pack()


    return 0

def pick_a_name(lst):
    
    if len(lst) == 0:
        popup("800x200", "\t     There are no more names in the hat...\n\tThanks for using me!", "", [], "Empty Hat")
        return []
    else:
        filtered = lst
        #run program here
        pickedname = rand.choice(filtered)
        popup("900x500", "  From " + str(len(filtered)) + " entries, the name pulled out is: ", pickedname, filtered, "Name Picked")
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
    main.iconbitmap("assets/pshico.ico")
    window_width = 900
    window_height = 250

    screenwidth = main.winfo_screenwidth()
    screenheight = main.winfo_screenheight()

    centre_x = int(screenwidth/2 - window_width/2)
    centre_y = int(screenheight/2 - window_height/2)

    main.geometry(f'{window_width}x{window_height}+{650}+{750}')

    main.configure(bg='#012456')

    label1 = ttk.Label(main, foreground='#fff', background='#012456', text=">Pick a Name from the Hat", font=('Terminal', 18))
    label2 = ttk.Label(main, foreground='#fff', background='#012456', text="Enter the file name: ", font=('Terminal'))
    label3 = ttk.Label(main, foreground='#fff', background='#012456', text=".xlsx", font='Terminal')
    filename = tk.StringVar()
    fileentry = ttk.Entry(main, textvariable=filename)
    
    label1.grid(row=0, column=1, padx=10, pady=20)
    label2.grid(row=1, column=1)
    label3.grid(row=1, column=3)
    fileentry.grid(row=1, column=2, padx=5)

    confirm = ttk.Button(main, text="Confirm", command=lambda : mainfunction(fileentry.get()))
    confirm.grid(row=5, column=2, padx=50, pady=50)

    main.mainloop()