import tkinter as tk

class Master_Window:
	def __init__(self, master):
      	self.master = master
        self.frame = tk.Frame(self.master)
		self.Style = Style()
		self.Style.theme_use('default')
		self.master.title('Theo´s testing GUI')
		self.pack(fill = BOTH, expand = 1)
		
		#Buttons
		#Windows
		self.bw2 = tk.Button(self.frame, text = 'Open window 2', width = 25, command = self.new_window)
		self.bw2.place(x = 150, y = 180)

		#Quit
		self.quitButton = Button(self.frame, text = 'Quit testing', command = self.quit)
		self.quitButton.place(x = 300, y = 290)

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

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2:
	def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
		self.Style = Style()
        self.Style.theme_use('default')
		self.master.title('Theo´s window2')
		self.master.geometry('400x400+200+200')
		lbl_title = Label(self, text='Theo´s testing GUI', font=("Helvetica", 16))
		lbl_title.place(x = 0, y = 0)
		self.qButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.qButton.pack()
    def close_windows(self):
        self.master.destroy()

def main():
	root = tk.Tk() 
	root.geometry('700x360+500+150')
	app = Master_Window(root)
	root.mainloop()

main()