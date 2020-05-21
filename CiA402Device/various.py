import tkinter as tk
from tkinter.ttk import *
from tkinter import BOTH
class Master_Window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Theo´s testing GUI')
        self.frame.pack(fill = BOTH, expand = 1)
        #Button to open window 2
        self.bw2 = tk.Button(self.frame, text = 'Open control window', width = 25, command = self.new_window2)
        self.bw2.place(x = 150, y = 180)
        #Button to open window 3
        self.bw3 = tk.Button(self.frame, text = 'Open error window', width = 25, command = self.new_window3)
        self.bw3.place(x = 10, y = 180)
    def new_window2(self):
        self.newWindow2 = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow2)
    def new_window3(self):
        self.newWindow3 = tk.Toplevel(self.master)
        self.app = Window3(self.newWindow3)

class Window2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

class Window3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk() 
    root.geometry('700x360+500+150')
    app = Master_Window(root)
    root.mainloop()


main()