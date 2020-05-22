import tkinter as tk
from tkinter.ttk import *
from tkinter import Tk, BOTH, IntVar, END
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



class Master_Window(Cia402device.CiA402Device):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Theo´s testing GUI')
        self.master.geometry('450x280+500+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Buttons
        #Button to open window 2
        self.bw2 = Button(self.frame, text = 'Open control window', width = 20, command = self.new_window2)
        self.bw2.place(x = 250, y = 130)
        #Button to open window 3
        self.bw3 = Button(self.frame, text = 'Open error window', width = 20, command = self.new_window3)
        self.bw3.place(x = 250, y = 180)
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit GUI', width = 15, command = self.master.quit)
        self.quitButton.place(x = 250, y = 230)
        #Reset and Switch ON
        self.resButton = Button(self.frame, text = 'Switch On', command = self.SwitchOn)
        self.resButton.place(x = 300, y =30)
        self.offButton = Button(self.frame, text = 'Switch Off', command = self.SwitchOff)
        self.offButton.place(x = 300, y =60)
        #Label
        lbl_title = Label(self.frame, text='Please, to start testing, switch on Teo:')
        lbl_title.place(x = 0, y = 30)
        lbl_off = Label(self.frame, text='Please, to stop testing, turn off Teo:')
        lbl_off.place(x = 0, y = 60)
        lbl = Label(self.frame, text='Once Teo is ON, open the testing window you want to use:')
        lbl.place(x = 0, y = 100)
        lblq = Label(self.frame, text='Once Teo is OFF, to quit the GUI app:')
        lblq.place(x = 0, y = 235)
        lblport = Label(self.frame, text='Before switching Teo ON entry the comm port:')
        lblport.place(x = 0, y = 0)
        #Entries:
        self.port = Entry(self.frame, width = 3)
        self.port.place(x = 310, y = 0)
        #Checkboxes
        self.var1 = IntVar()        
        self.check_switchon = Checkbutton(self.frame,  variable = self.var1)
        self.check_switchon.place(x = 400, y = 30)
        self.var2 = IntVar()        
        self.check_switchoff = Checkbutton(self.frame, variable = self.var2)
        self.check_switchoff.place(x = 400, y = 60)


    def new_window2(self):
        self.newWindow2 = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow2)
    def new_window3(self):
        self.newWindow3 = tk.Toplevel(self.master)
        self.app = Window3(self.newWindow3)

    def SwitchOn(self):
        global porter
        porter = int(self.port.get())
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(porter, pm1);
        cia402.Reset()
        cia402.SwitchOn();
        self.var1.set(True)
        self.var2.set(False)
    def SwitchOff(self):
        port = int(self.port.get())
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        cia402.SwitchOff();
        self.var1.set(False)
        self.var2.set(True)
        self.port.delete('0', END)

class Window2(Cia402device.CiA402Device):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Theo´s control window')
        self.master.geometry('700x360+800+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Buttons
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit', command = self.master.destroy)
        self.quitButton.place(x = 300, y = 290)
        #Position
        self.p_b = Button(self.frame, text = 'Get Position', command = self.position)
        self.p_b.place(x = 450, y = 50)
        #Velocity
        self.v_b = Button(self.frame, text = 'Get Velocity', command = self.velocity)
        self.v_b.place(x = 450, y = 100)
        #Mean Velocity
        self.mv_b = Button(self.frame, text = 'Get Mean Velocity', command = self.mean_velocity)
        self.mv_b.place(x = 450, y = 150)
        #Get Amps
        self.amps_b = Button(self.frame, text = 'Get Amps', command = self.amps)
        self.amps_b.place(x = 450, y = 200)
        #Get filtered amps
        self.famps_b = Button(self.frame, text = 'Get filtered amps', command = self.filtered_amps)
        self.famps_b.place(x = 450, y = 250)
        #textboxes
        self.velocity = Entry(self.frame, width = 10)
        self.velocity.place(x = 570, y = 100)
        self.position = Entry(self.frame, width = 10)
        self.position.place(x = 570, y = 50)
        self.meanvelocity = Entry(self.frame, width = 10)
        self.meanvelocity.place(x = 570, y = 150)
        self.amps = Entry(self.frame, width = 10)
        self.amps.place(x = 570, y = 200)
        self.filtamps = Entry(self.frame, width = 10)
        self.filtamps.place(x = 570, y = 250)
        #Labels 
        lbl1 = Label(self.frame, text = 'Position:')
        lbl1.place(x = 570, y = 30)
        lbl2 = Label(self.frame, text = 'Velocity:')
        lbl2.place(x = 570, y = 80)
        lbl3 = Label(self.frame, text = 'Mean Velocity:')
        lbl3.place(x = 570, y = 130)
        lbl4 = Label(self.frame, text = 'Amps:')
        lbl4.place(x = 570, y = 180)
        lbl5 = Label(self.frame, text = 'Filtered amps:')
        lbl5.place(x = 570, y = 230)
        lbl6 = Label(self.frame, text = 'Simulation data:')
        lbl6.place(x = 450, y = 30)

    def position(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        pos = cia402.GetPosition(); 
        self.position.delete('0', END)
        self.position.insert(0, str(pos)) 
        

    def velocity(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        vel = cia402.GetVelocity();
        self.velocity.delete('0', END)
        self.velocity.insert(0, str(vel)) 
        
    def mean_velocity(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        mean_vel = cia402.GetMeanVelocity();        
        self.meanvelocity.delete('0', END)
        self.meanvelocity.insert(0, str(mean_vel)) 
        
    def amps(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        amps = cia402.GetAmps();
        self.amps.delete('0', END)
        self.amps.insert(0, str(amps)) 
    
    def filtered_amps(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        famp = cia402.GetFilterdAmps();
        self.filtamps.delete('0', END)
        self.filtamps.insert(0, str(famp)) 

    def SwitchOn(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        cia402.Reset()
        cia402.SwitchOn();
        self.var1.set(True)

class Window3:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
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
