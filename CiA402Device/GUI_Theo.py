#Vamos a usar traits library
import numpy as np
import Cia402device
"""
Import clase Tkinter:
	Tk class: Crea ventana
	Frame class: Clase raiz que contiene los widgets necesarios, lo hereda la clase GUI
"""

from tkinter import Tk, BOTH
from tkinter.ttk import *

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




class gui_example(Frame):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.Style = Style()
		self.Style.theme_use('default')
		self.master.title('Prueba')
		self.pack(fill = BOTH, expand = 1)
		
		#Buttons
		quitButton = Button(self, text = 'Quit GUI', command = self.quit)
		quitButton.place(x = 90, y = 130)
		c_b = Button(self, text = 'Calculate', command = self.calculator)
		c_b.place(x = 90, y = 70)
		
		#textboxes
		self.rate = Entry(self, width = 10)
		self.rate.place(x = 150, y = 40)
		self.name = Entry(self, width = 10)
		self.name.place(x = 10, y = 40)

		#Labels 
		lbl_title = Label(self, text='Short rate GUI', font=("Helvetica", 16))
		lbl_title.place(x = 80, y = 0)
		lbl1 = Label(self, text = 'Name:')
		lbl1.place(x = 10, y = 20)
		lbl2 = Label(self, text = 'Rate:')
		lbl2.place(x = 150, y = 20)

	def calculator(self):
		self.rate = self.rate.get()
		self.name = self.name.get()
		sr = short_rate(self.name, float(self.rate))
		time_list = [0.0, 0.5, 1.0, 1.25, 1.75, 2.0]
		dscnt = sr.get_discount_factors(time_list)
		result = dscnt[0]
		self.lbl_out = Label(self, text = str(result))
		self.lbl_out.place(x = 120, y = 100)



"""
Una vez creada la clase, creo el main para lanzar la GUI, a traves de una función:
	1º Creo la root window, que es la ventana de la aplicación. Debe ser la primera en ser creada siempre
	2º Defino la geometria: Anchura x Altura + posición x + posición y (en pantalla)
	3º Instancio la clase de la GUI
	4º Lanzo el mainloop, siempre es el paso final, o el refresco de pantalla
"""


def main():
	root = Tk() 
	root.geometry('260x160+1000+350')
	app = gui_example()

	root.mainloop()

main()
