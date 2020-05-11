from tkinter import Tk, BOTH
from tkinter.ttk import *
import Cia402device

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




class gui_example(Frame, Cia402device.CiA402Device):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.Style = Style()
		self.Style.theme_use('default')
		self.master.title('Theo´s testing GUI')
		self.pack(fill = BOTH, expand = 1)
		
		#Buttons
		quitButton = Button(self, text = 'Quit testing', command = self.quit)
		quitButton.place(x = 90, y = 140)
		p_b = Button(self, text = 'Get Position', command = self.position)
		p_b.place(x = 10, y = 80)
		v_b = Button(self, text = 'Get Velocity', command = self.velocity)
		v_b.place(x = 150, y = 80)
		#textboxes
		self.velocity = Entry(self, width = 10)
		self.velocity.place(x = 150, y = 50)
		self.position = Entry(self, width = 10)
		self.position.place(x = 10, y = 50)

		#Labels 
		lbl_title = Label(self, text='Theo´s testing GUI', font=("Helvetica", 16))
		lbl_title.place(x = 40, y = 0)
		lbl1 = Label(self, text = 'Position:')
		lbl1.place(x = 10, y = 30)
		lbl2 = Label(self, text = 'Velocity:')
		lbl2.place(x = 150, y = 30)

	def position(self):
		cia402_pos = Cia402device.CiA402Device();
		pos = cia402_pos.GetPosition();		
		self.position.insert(str(pos)) 
		

	def velocity(self):
		cia402_vel = Cia402device.CiA402Device();
		vel = cia402_vel.GetVelocity();
		self.velocity.insert(str(vel)) 
		


"""
Una vez creada la clase, creo el main para lanzar la GUI, a traves de una función:
	1º Creo la root window, que es la ventana de la aplicación. Debe ser la primera en ser creada siempre
	2º Defino la geometria: Anchura x Altura + posición x + posición y (en pantalla)
	3º Instancio la clase de la GUI
	4º Lanzo el mainloop, siempre es el paso final, o el refresco de pantalla
"""


def main():
	root = Tk() 
	root.geometry('250x180+300+150')
	app = gui_example()

	root.mainloop()

main()
