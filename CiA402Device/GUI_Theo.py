import tkinter as tk
from tkinter.ttk import *
from tkinter import Tk, BOTH, IntVar, END, Text
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
        #Stop/Start Simulation
        self.ssb = Button(self.frame, text = 'Stop/Start Simulation', command = lambda : self.loop(True))
        self.ssb.place(x = 410, y = 10)
        #Set Velocity
        self.svel = Button(self.frame, text = 'Set Velocity', command = self.bsvel)
        self.svel.place(x = 100, y = 130)
        #Set Position
        self.svel = Button(self.frame, text = 'Set Position', command = self.bspos)
        self.svel.place(x = 100, y = 230)
        #Set Torque
        self.svel = Button(self.frame, text = 'Set Torque', command = self.bstorque)
        self.svel.place(x = 100, y = 180)
        #textboxes
        self.sample = Entry(self.frame, width = 10)
        self.sample.place(x = 250, y = 130)
        self.time_frame = Entry(self.frame, width = 10)
        self.time_frame.place(x = 350, y = 130)
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
        pltlbl3 = Label(self.frame, text = 'Sample time:')
        pltlbl3.place(x = 250, y = 110)
        pltlbl1 = Label(self.frame, text = 'Plot time frame:')
        pltlbl1.place(x = 350, y = 110)
        pltlbl2 = Label(self.frame, text = 'Simulation plot:')
        pltlbl2.place(x = 250, y = 90)
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
        self.check_t = Checkbutton(self.frame, text = 'Torque mode',  variable = self.vart, command = self.torquemode)
        self.check_t.place(x = 0, y = 60)
        #pos graph
        self.varpg = IntVar()        
        self.graph_p = Checkbutton(self.frame, text = 'Check to graph position when simulating',  variable = self.varpg)
        self.graph_p.place(x = 250, y = 160)
        global measures
        measures = list()
    def get_position(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        pos = cia402.GetPosition(); 
        self.position.delete('0', END)
        self.position.insert(0, str(pos)) 
        measures.append(pos)

    def get_velocity(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        vel = cia402.GetVelocity();
        self.velocity.delete('0', END)
        self.velocity.insert(0, str(vel)) 
        
    def get_mean_velocity(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        mean_vel = cia402.GetMeanVelocity();        
        self.meanvelocity.delete('0', END)
        self.meanvelocity.insert(0, str(mean_vel)) 
        
    def get_amps(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        amps = cia402.GetAmps();
        self.amps.delete('0', END)
        self.amps.insert(0, str(amps)) 
    
    def get_filtered_amps(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        famp = cia402.GetFilterdAmps();
        self.filtamps.delete('0', END)
        self.filtamps.insert(0, str(famp)) 

    def bsvel(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        veloc = float(self.setvel.get())
        cia402.SetVelocity(veloc)
    
    def bstorque(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        torq = float(self.settorq.get())
        cia402.SetTorque(torq)
    
    def bspos(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        posit = float(self.setpos.get())
        cia402.SetPosition(posit)


    def posmode(self):
        self.varv.set(False)
        self.vart.set(False)
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        cia402.SetupPositionMode();

    def velmode(self):
        self.varp.set(False)
        self.vart.set(False)
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        cia402.Setup_Velocity_Mode(); 

    def torquemode(self):
        self.varv.set(False)
        self.varp.set(False)
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        cia402.Setup_Torque_Mode();

    def loop(self, toggle=False):
        global tracking_var
        if toggle:
            if tracking_var:
                tracking_var = False
            else:
                tracking_var = True


        if tracking_var:
            
            self.get_position()
            self.get_velocity()
            self.get_mean_velocity()
            self.get_amps()
            self.get_filtered_amps()
            print(measures)
            tsamp = self.sample.get()
            print(tsamp)
            self.frame.after(1000, self.loop) #1000 es el numero de milisegundos que dura el intervalo entre la llamada a la función loop

class Window3(Cia402device.CiA402Device):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Theo´s error window')
        self.master.geometry('630x400+100+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit error window.', command = self.master.destroy)
        self.quitButton.place(x = 200, y = 350)
        #Get Msg
        self.gmsg = Button(self.frame,text = 'Get error message.', command = lambda : self.loop_msg(True))
        self.gmsg.place(x = 10, y = 350)
        #Labels 
        lbl1 = Label(self.frame, text = 'Can id:')
        lbl1.place(x = 10, y = 30)
        lbl4 = Label(self.frame, text = 'Error type:')
        lbl4.place(x = 10, y = 260)
        lbl5 = Label(self.frame, text = 'Error:')
        lbl5.place(x = 10, y = 300)
        lbl6 = Label(self.frame, text = 'Filter messages by first number:')
        lbl6.place(x = 410, y = 30)
        #textboxes
        #self.canid = Entry(self.frame, width = 40)
        self.canid = Text(self.frame, width = 40)
        self.canid.place(x = 60, y = 30, height = 220)
        self.err_typ = Entry(self.frame, width = 10)
        self.err_typ.place(x = 80, y = 260)
        self.errrr = Entry(self.frame, width = 20)
        self.errrr.place(x = 50, y = 300)
        #Checkboxes
        # error, 0
        self.var0 = IntVar()        
        self.check_0 = Checkbutton(self.frame, text = '0',  variable = self.var0)
        self.check_0.place(x = 410, y = 50)
        # error, 1
        self.var1 = IntVar()        
        self.check_1 = Checkbutton(self.frame, text = '1', variable = self.var1)
        self.check_1.place(x = 410, y = 70)
        # error, 2
        self.var2 = IntVar()        
        self.check_2 = Checkbutton(self.frame, text = '2',  variable = self.var2)
        self.check_2.place(x = 410, y = 90)
        # error, 3
        self.var3 = IntVar()        
        self.check_3 = Checkbutton(self.frame, text = '3',  variable = self.var3)
        self.check_3.place(x = 410, y = 110)
        # error, 4
        self.var4 = IntVar()        
        self.check_4 = Checkbutton(self.frame, text = '4', variable = self.var4)
        self.check_4.place(x = 410, y = 140)
        # error, 5
        self.var5 = IntVar()        
        self.check_5 = Checkbutton(self.frame, text = '5',  variable = self.var5)
        self.check_5.place(x = 410, y = 170)
        # error, 6
        self.var6 = IntVar()        
        self.check_6 = Checkbutton(self.frame, text = '6', variable = self.var6)
        self.check_6.place(x = 410, y = 200)
        # error, 7
        self.var7 = IntVar()        
        self.check_7 = Checkbutton(self.frame, text = '7',  variable = self.var7)
        self.check_7.place(x = 410, y = 230)
        # error, 8
        self.var8 = IntVar()        
        self.check_8 = Checkbutton(self.frame, text = '8',  variable = self.var8)
        self.check_8.place(x = 410, y = 260)
        # error, 9
        self.var9 = IntVar()        
        self.check_9 = Checkbutton(self.frame, text = '9', variable = self.var9)
        self.check_9.place(x = 410, y = 290)
        #error, F
        self.varF = IntVar()        
        self.check_F = Checkbutton(self.frame, text = 'F',  variable = self.varF)
        self.check_F.place(x = 410, y = 320)

        global pm1
        pm1 = SocketCanPort.SocketCanPort("can1")


    def getmsg(self):
        #Obtengo lo nuevo
        err,cid,dat,siz = pm1.GetMsg()
        lister = self.checkbox_check()
        #Inserto lo nuevo solo si está marcado:
        for i in range(0,len(lister)):
            if str(lister[i]) == str(hex(cid))[2]:
                filtered = True
                break
            else:
                filtered = False
        if filtered == True:
            msg = 'Cid: ' + str(hex(cid)) + ', Data: ' + str(dat) + ', Size: ' +str(siz)
            self.canid.insert(END, msg + '\n')
            self.err_typ.delete('0', END)
            self.err_typ.insert(0, str(err))
        if err == -1:
            self.errrr.delete('0', END)
            self.errrr.insert(0, 'Timeout in poll read.')
        elif err == -2:
            self.errrr.delete('0', END)
            self.errrr.insert(0, 'Error in poll read.')
        elif err == 0:
            self.errrr.delete('0', END)

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

    def checkbox_check(self):
        lis = list()
        if self.var0.get() == 1:
            lis.append('0')
        if self.var1.get() == 1:
            lis.append('1')
        if self.var2.get() == 1:
            lis.append('2')
        if self.var3.get() == 1:
            lis.append('3')
        if self.var4.get() == 1:
            lis.append('4')
        if self.var5.get() == 1:
            lis.append('5')
        if self.var6.get() == 1:
            lis.append('6')
        if self.var7.get() == 1:
            lis.append('7')
        if self.var8.get() == 1:
            lis.append('8')
        if self.var9.get() == 1:
            lis.append('9')
        if self.varF.get() == 1:
            lis.append('F')
        return lis





def main(): 
    root = tk.Tk() 
    app = Master_Window(root)
    root.mainloop()


tracking_var = False
main()
