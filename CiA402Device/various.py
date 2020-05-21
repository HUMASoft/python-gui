import tkinter as tk
from tkinter.ttk import *
from tkinter import BOTH, END
class Master_Window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Theo´s testing GUI')
        self.master.geometry('700x360+500+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Buttons
        #Button to open window 2
        self.bw2 = tk.Button(self.frame, text = 'Open control window', width = 25, command = self.new_window2)
        self.bw2.place(x = 300, y = 180)
        #Button to open window 3
        self.bw3 = tk.Button(self.frame, text = 'Open error window', width = 25, command = self.new_window3)
        self.bw3.place(x = 10, y = 180)
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit testing', width = 25, command = self.master.quit)
        self.quitButton.place(x = 200, y = 290)

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
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Theo´s control window')
        self.master.geometry('700x360+800+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit', command = self.master.destroy)
        self.quitButton.place(x = 100, y = 290)
        #Position
        self.p_b = Button(self.frame, text = 'Get Position', command = self.position)
        self.p_b.place(x = 10, y = 180)

        #textboxes
        self.position = Entry(self.frame, width = 10)
        self.position.place(x = 10, y = 150)
        self.port = Entry(self.frame, width = 10)
        self.port.place(x = 10, y = 100)
        
        #Labels 
        self.lbl_title = Label(self.frame, text='Theo´s testing GUI', font=("Helvetica", 16))
        self.lbl_title.place(x = 280, y = 0)
        self.lbl1 = Label(self.frame, text = 'Position:')
        self.lbl1.place(x = 10, y = 130)

    def position(self):
        pos = int(self.port.get())
        self.position.delete('0', END)      
        self.position.insert(0, str(pos)) 

class Window3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Theo´s error window')
        self.master.geometry('700x360+100+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit', command = self.master.destroy)
        self.quitButton.place(x = 100, y = 290)

def main(): 
    root = tk.Tk() 
    app = Master_Window(root)
    root.mainloop()


main()