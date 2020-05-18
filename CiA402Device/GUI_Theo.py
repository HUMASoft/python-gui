from tkinter import Tk, BOTH, IntVar
from tkinter.ttk import *
import SocketCanPort
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
		quitButton.place(x = 300, y = 290)
		#Position
		p_b = Button(self, text = 'Get Position', command = self.position)
		p_b.place(x = 10, y = 180)
		#Velocity
		v_b = Button(self, text = 'Get Velocity', command = self.velocity)
		v_b.place(x = 150, y = 180)
		#Mean Velocity
		mv_b = Button(self, text = 'Get Mean Velocity', command = self.mean_velocity)
		mv_b.place(x = 275, y = 180)
		#Get Amps
		amps_b = Button(self, text = 'Get Amps', command = self.amps)
		amps_b.place(x = 450, y = 180)
		#Get filtered amps
		famps_b = Button(self, text = 'Get filtered amps', command = self.filtered_amps)
		famps_b.place(x = 570, y = 180)
		#Reset and Switch ON
		resButton = Button(self, text = 'Switch On', command = self.SwitchOn)
		resButton.place(x = 10, y =40)
		#Checkboxes
		self.var1 = IntVar()		
		self.check_switch = Checkbutton(self, variable = self.var1)
		self.check_switch.place(x = 100, y = 70)		
		
        
		#textboxes
		self.velocity = Entry(self, width = 10)
		self.velocity.place(x = 150, y = 150)
		self.position = Entry(self, width = 10)
		self.position.place(x = 10, y = 150)
		self.meanvelocity = Entry(self, width = 12)
		self.meanvelocity.place(x = 290, y = 150)
		self.amps = Entry(self, width = 10)
		self.amps.place(x = 450, y = 150)
		self.filtamps = Entry(self, width = 10)
		self.filtamps.place(x = 570, y = 150)
		#Labels 
		lbl_title = Label(self, text='Theo´s testing GUI', font=("Helvetica", 16))
		lbl_title.place(x = 280, y = 0)
		lbl1 = Label(self, text = 'Position:')
		lbl1.place(x = 10, y = 130)
		lbl2 = Label(self, text = 'Velocity:')
		lbl2.place(x = 150, y = 130)
		lbl3 = Label(self, text = 'Mean Velocity:')
		lbl3.place(x = 290, y = 130)
		lbl4 = Label(self, text = 'Amps:')
		lbl4.place(x = 450, y = 130)
		lbl5 = Label(self, text = 'Filtered amps:')
		lbl5.place(x = 570, y = 130)
		lblswitch = Label(self, text = 'Switched on:')
		lblswitch.place(x = 10, y = 70)

	def position(self):
		pos = cia402.GetPosition();	
		self.position.insert(0, str(pos)) 
		

	def velocity(self):
		vel = cia402.GetVelocity();
		self.velocity.insert(0, str(vel)) 
		
	def mean_velocity(self):
		mean_vel = cia402.GetMeanVelocity();		
		self.meanvelocity.insert(0, str(mean_vel)) 
		
	def amps(self):
		amps = cia402.GetAmps();
		self.amps.insert(0, str(amps)) 
	
	def filtered_amps(self):
		famp = cia402.GetFilterdAmps();
		self.filtamps.insert(0, str(famp)) 

	def SwitchOn(self):
		pm1 = SocketCanPort.SocketCanPort("can1")
		cia402 = Cia402device.CiA402Device(31, pm1);
		cia402.Reset()
		cia402.SwitchOn();
		self.var1.set(True)


"""
Una vez creada la clase, creo el main para lanzar la GUI, a traves de una función:
	1º Creo la root window, que es la ventana de la aplicación. Debe ser la primera en ser creada siempre
	2º Defino la geometria: Anchura x Altura + posición x + posición y (en pantalla)
	3º Instancio la clase de la GUI
	4º Lanzo el mainloop, siempre es el paso final, o el refresco de pantalla
"""


def main():
	root = Tk() 
	root.geometry('700x360+500+150')
	
	app = gui_example()
	
	root.mainloop()

main()
