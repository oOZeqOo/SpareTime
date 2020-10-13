import tkinter as tk
from tkinter import messagebox, simpledialog


def getInput(x, width):
    number = '0'
    options = ["A* Algorithm", "Dijkstras Algorithm",]

    root = tk.Tk()

    tk.Label(root, text = "Choose an algorithm to path find!").pack(side = 'top')

    clicked = tk.StringVar()
    clicked.set(options[0])
    drop = tk.OptionMenu(root, clicked, *options)
    drop.pack()

    #var1 = IntVar()
    #Checkbutton(master, text="male", variable=var1).grid(row=0, sticky=W)

    def onApplySettings():
        root.destroy()

    tk.Button(root, command=onApplySettings, text = 'Apply Settings').pack(side = 'bottom')
    root.geometry("200x150+{}+{}".format(x + width, x) )
    root.mainloop()
    return clicked.get()
