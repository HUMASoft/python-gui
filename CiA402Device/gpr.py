import tkinter
from tkinter import * 
from tkinter.ttk import *


"""
Import clase Tkinter:
	Tk class: Crea ventana
	Frame class: Clase raiz que contiene los widgets necesarios, lo hereda la clase GUI
"""



""" 
A continuación creo la clase de la GUI, que hereda los widgets de Frame.
Pasos:
__init__:
	- __init__ es el constructor de la clase de la gui, y llamamos a super().__init__(), que es el constructor de Frame. 
	- Con self.initUI() delegamos la creación de la interfaz a la clase heredada.
initUI:
	- con .master.title() damos titulo a la ventana. Al usar master doy acceso a Tk
	- .pack es uno de los organizadores de la ventana. Organiza la ventana en cuadrados 
	- Creo botones con Button() 
"""





class Master_Window(Frame):
	def __init__(self):
		super().__init__()
		self.butnew('Open window 2', '2', Window2)
		self.butnew('Open window 3', '3', Window3)
		self.Style = Style()
		self.Style.theme_use('default')
		self.master.title('Theo´s testing GUI')
		self.pack(fill = BOTH, expand = 1)
		#Buttons
		quitButton = Button(self, text = 'Quit testing', command = self.quit)
		quitButton.place(x = 300, y = 290)
		#Position
		p_b = Button(self, text = 'Get Position', command = self.position)
		p_b.place(x = 10, y = 180)
		#textboxes
		self.position = Entry(self, width = 10)
		self.position.place(x = 10, y = 150)
		self.port = Entry(self, width = 10)
		self.port.place(x = 10, y = 100)
		#Labels 
		lbl_title = Label(self, text='Theo´s testing GUI', font=("Helvetica", 16))
		lbl_title.place(x = 280, y = 0)
		lbl1 = Label(self, text = 'Position:')
		lbl1.place(x = 10, y = 130)

	def position(self):
		pos = int(self.port.get())
		self.position.delete('0', END)		
		self.position.insert(0, str(pos)) 

	def SwitchOn(self):
		port = int(self.port.get())

	def butnew(self, text, number, _class):
		tkinter.Button(self, text = text, command = lambda: self.new_window(number, _class)).pack()	

	def new_window(self, number, _class):
			self.new = tkinter.Toplevel(self.master)
			_class(self.new, number)

	
	

class Window2:
	def __init__(self, master, number):
		self.Style = Style()
		self.Style.theme_use('default')
		self.master.title('Theo´s window2')
		self.geometry('400x400+200+200')
		self.pack(fill = BOTH, expand = 1)

class Window3:
	def __init__(self, master, number):
		self.Style = Style()
		self.Style.theme_use('default')
		self.master.title('Theo´s window2')
		self.geometry('400x400+200+200')
		self.pack(fill = BOTH, expand = 1)



		



"""
Una vez creada la clase, creo el main para lanzar la GUI, a traves de una función:
	1º Creo la root window, que es la ventana de la aplicación. Debe ser la primera en ser creada siempre
	2º Defino la geometria: Anchura x Altura + posición x + posición y (en pantalla)
	3º Instancio la clase de la GUI
	4º Lanzo el mainloop, siempre es el paso final, o el refresco de pantalla
"""


def main():
	root = tkinter.Tk() 
	root.geometry('700x360+500+150')
	app = Master_Window()
	root.mainloop()

main()
