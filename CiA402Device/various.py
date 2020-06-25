import tkinter as tk
from tkinter.ttk import *
from tkinter import Tk, BOTH, IntVar, END

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



class Master_Window:
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
        self.bw2 = Button(self.frame, text = 'Open control window', width = 15, command = self.new_window2)
        self.bw2.place(x = 250, y = 130)
        #Button to open window 3
        self.bw3 = Button(self.frame, text = 'Open error window', width = 15, command = self.new_window3)
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

    def SwitchOn(self):
        global porter
        porter = int(self.port.get())
        self.var1.set(True)
        self.var2.set(False)
    def SwitchOff(self):
        self.var1.set(False)
        self.var2.set(True)
        self.port.delete('0', END)
    def new_window2(self):
        self.newWindow2 = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow2)
    def new_window3(self):
        self.newWindow3 = tk.Toplevel(self.master)
        self.app = Window3(self.newWindow3)

class Window2(Master_Window):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Theo´s control window')
        self.master.geometry('700x360+800+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit', command = self.master.destroy)
        self.quitButton.place(x = 300, y = 290)
        #Stop/Start Simulation
        self.ssb = Button(self.frame, text = 'Stop/Start Simulation', command = lambda : self.loop(True))
        self.ssb.place(x = 410, y = 10)
        #Set Velocity
        self.svel = Button(self.frame, text = 'Set Velocity', command = self.get_position)
        self.svel.place(x = 100, y = 130)
        #Set Position
        self.svel = Button(self.frame, text = 'Set Position', command = self.get_position)
        self.svel.place(x = 100, y = 230)
        #Set Torque
        self.svel = Button(self.frame, text = 'Set Torque', command = self.get_position)
        self.svel.place(x = 100, y = 180)
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
        self.setvel = Entry(self.frame, width = 10)
        self.setvel.place(x = 0, y = 130)
        self.settorq = Entry(self.frame, width = 10)
        self.settorq.place(x = 0, y = 180)
        self.setpos = Entry(self.frame, width = 10)
        self.setpos.place(x = 0, y = 230)
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
        lbl6.place(x = 410, y = 40)
        lbl7 = Label(self.frame, text = 'Simulation setup data:')
        lbl7.place(x = 0, y = 90)
        lbl8 = Label(self.frame, text = 'Velocity:')
        lbl8.place(x = 0, y = 110)
        lbl9 = Label(self.frame, text = 'Torque:')
        lbl9.place(x = 0, y = 160)
        lbl10 = Label(self.frame, text = 'Position:')
        lbl10.place(x = 0, y = 210)
        lbl11 = Label(self.frame, text = 'Simulation mode:')
        lbl11.place(x = 0, y = 0)
        #Checkboxes
        #pos mode
        self.varp = IntVar()        
        self.check_p = Checkbutton(self.frame, text = 'Position mode',  variable = self.varp, command = self.posmode)
        self.check_p.place(x = 0, y = 20)
        #vel mode
        self.varv = IntVar()        
        self.check_v = Checkbutton(self.frame, text = 'Velocity mode', variable = self.varv, command = self.velmode)
        self.check_v.place(x = 0, y = 40)
        #torquemode
        self.vart = IntVar()        
        self.check_t = Checkbutton(self.frame, text = 'Torque mode',  variable = self.vart, command = self.tormode)
        self.check_t.place(x = 0, y = 60)
        #counter
        self.cont = 0

    def get_position(self):
        self.cont = self.cont + 1
        pos = self.cont
        self.position.delete('0', END)      
        self.position.insert(0, str(pos)) 

    def loop(self, toggle=False):
        global tracking_var
        if toggle:
            if tracking_var:
                tracking_var = False
            else:
                tracking_var = True


        if tracking_var:
            self.get_position()
            self.frame.after(1000, self.loop) #1000 es el numero de milisegundos que dura el intervalo entre la llamada a la función loop

    def posmode(self):
        print('pos mode')
        self.varv.set(False)
        self.vart.set(False)

    def velmode(self):
        print('vel mode')
        self.varp.set(False)
        self.vart.set(False)

    def tormode(self):
        print('torque mode')
        self.varv.set(False)
        self.varp.set(False)

class Window3:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Theo´s error window')
        self.master.geometry('380x280+100+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit error window.', command = self.master.destroy)
        self.quitButton.place(x = 170, y = 140)
        #Get Msg
        #Stop/Start Simulation
        self.gmsg = Button(self.frame,text = 'Get error message.', command = lambda : self.loop_msg(True))
        self.gmsg.place(x = 170, y = 90)
        #Labels 
        lbl1 = Label(self.frame, text = 'Can id:')
        lbl1.place(x = 10, y = 30)
        lbl2 = Label(self.frame, text = 'Data:')
        lbl2.place(x = 10, y = 80)
        lbl3 = Label(self.frame, text = 'Size:')
        lbl3.place(x = 10, y = 130)
        lbl4 = Label(self.frame, text = 'Error type:')
        lbl4.place(x = 10, y = 180)
        lbl5 = Label(self.frame, text = 'Error:')
        lbl5.place(x = 10, y = 230)
        #textboxes
        self.canid = Entry(self.frame, width = 10)
        self.canid.place(x = 60, y = 30)
        self.dat = Entry(self.frame, width = 10)
        self.dat.place(x = 50, y = 80)
        self.siz = Entry(self.frame, width = 10)
        self.siz.place(x = 50, y = 130)
        self.err_typ = Entry(self.frame, width = 10)
        self.err_typ.place(x = 80, y = 180)
        self.errrr = Entry(self.frame, width = 10)
        self.errrr.place(x = 50, y = 230)
        self.cont = 0

    def loop_msg(self, toggle=False):
        global tracking_var
        if toggle:
            if tracking_var:
                tracking_var = False
            else:
                tracking_var = True


        if tracking_var:
            self.getmsg()
            self.frame.after(1000, self.loop_msg) #1000 es el numero de milisegundos que dura el intervalo entre la llamada a la función loop
    def getmsg(self):
        self.cont = self.cont + 1
        pos = self.cont
        self.canid.delete('0', END)      
        self.canid.insert(0, str(pos)) 

def main(): 
    root = tk.Tk() 
    app = Master_Window(root)
    root.mainloop()

tracking_var = False
main()
