import tkinter as tk
from tkinter.ttk import *
from tkinter import Tk, BOTH, IntVar, END, Text, font
import SocketCanPort
import Cia402device
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import tkinter.font as font

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
        helv36 = font.Font(family="Helvetica",size=36,weight="bold")        
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Teo´s testing GUI')
        self.master.geometry('450x280+500+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Buttons
        #Button to open window 2
        self.bw2 = Button(self.frame, text = 'Open control window', width = 20, command = self.new_window2)
        self.bw2.place(x = 250, y = 130)
        self.bw2['state'] = 'disabled'
        #Button to open window 3
        self.bw3 = Button(self.frame, text = 'Open error window', width = 20, command = self.new_window3)
        self.bw3.place(x = 250, y = 180)
        self.bw3['state'] = 'disabled'
        self.bconn = Button(self.frame, text = 'Connect port', width = 11, command = self.check_conn)
        self.bconn.place(x = 296, y = 0)
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit GUI', width = 15, command = self.master.quit)
        self.quitButton.place(x = 250, y = 230)
        #Reset and Switch ON
        self.resButton = Button(self.frame, text = 'Switch On', width = 11, command = self.SwitchOn)
        self.resButton.place(x = 296, y =30)
        self.resButton['state'] = 'disabled'
        self.offButton = Button(self.frame, text = 'Switch Off', width = 11, command = self.SwitchOff)
        self.offButton.place(x = 296, y =60)
        self.offButton['state'] = 'disabled'
        #Label
        lbl_title = Label(self.frame, text='Please, to start testing, switch on Teo:')
        lbl_title.place(x = 0, y = 30)
        lbl_off = Label(self.frame, text='Please, to stop testing, turn off Teo:')
        lbl_off.place(x = 0, y = 60)
        lbl = Label(self.frame, text='Once Teo is ON, open the testing window you want to use:')
        lbl.place(x = 0, y = 100)
        lblq = Label(self.frame, text='Once Teo is OFF, quit the GUI app:')
        lblq.place(x = 0, y = 235)
        lblport = Label(self.frame, text='Before switching Teo ON entry the id:')
        lblport.place(x = 0, y = 0)
        #Entries:
        self.port = Entry(self.frame, width = 3)
        self.port.place(x = 250, y = 0)
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

    def check_conn(self):
        port = (self.port.get())
        if self.port.get() == "" :
            aaaa = 2
        elif int(port) == 1 or int(port) == 2 or int(port) == 3:
            self.bw2['state'] = 'active'
            self.bw3['state'] = 'active'
            self.resButton['state'] = 'active'
            self.offButton['state'] = 'active'
        else:
            aaaaa = 2




class Window2(Cia402device.CiA402Device):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Teo´s control window')
        self.master.geometry('800x400+400+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Buttons
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit', command = self.master.destroy)
        self.quitButton.place(x = 380, y = 350)

        #Stop/Start Simulation
        self.ssb = Button(self.frame, text = 'Start/Stop Execution', command = lambda : self.loop(True))
        self.ssb.place(x = 600, y = 20)
        #Set Velocity
        self.svel = Button(self.frame, text = 'Set Velocity', width = 10, command = self.bsvel)
        self.svel.place(x = 270, y = 65)
        self.svel['state'] = 'disabled'
        #Set Position
        self.spos = Button(self.frame, text = 'Set Position', width = 10, command = self.bspos)
        self.spos.place(x = 270, y = 25)
        self.spos['state'] = 'disabled'
        #Set Torque
        self.stor = Button(self.frame, text = 'Set Torque', width = 10, command = self.bstorque)
        self.stor.place(x = 270, y = 105)
        self.stor['state'] = 'disabled'
        #textboxes
        self.sample = Entry(self.frame, width = 10)
        self.sample.place(x = 0, y = 240)
        self.exec_time = Entry(self.frame, width = 10)
        self.exec_time.place(x = 0, y = 190)
        self.time_frame = Entry(self.frame, width = 10)
        self.time_frame.place(x = 0, y = 290)
        self.velocity = Entry(self.frame, width = 10)
        self.velocity.place(x = 600, y = 140)
        self.position = Entry(self.frame, width = 10)
        self.position.place(x = 600, y = 90)
        self.meanvelocity = Entry(self.frame, width = 10)
        self.meanvelocity.place(x = 600, y = 190)
        self.amps = Entry(self.frame, width = 10)
        self.amps.place(x = 600, y = 240)
        self.filtamps = Entry(self.frame, width = 10)
        self.filtamps.place(x = 600, y = 290)
        self.setvel = Entry(self.frame, width = 3)
        self.setvel.place(x = 240, y = 70)
        self.settorq = Entry(self.frame, width = 3)
        self.settorq.place(x = 240, y = 110)
        self.setpos = Entry(self.frame, width = 3)
        self.setpos.place(x = 240, y = 30)
        #Labels 
        lbl1 = Label(self.frame, text = 'Position [rad]:', foreground="white")
        lbl1.place(x = 600, y = 70)
        lbl2 = Label(self.frame, text = 'Velocity [rad/s]:', foreground="white")
        lbl2.place(x = 600, y = 120)
        lbl3 = Label(self.frame, text = 'Mean Velocity [rad/s]:', foreground="white")
        lbl3.place(x = 600, y = 170)
        lbl4 = Label(self.frame, text = 'Amps:', foreground="white")
        lbl4.place(x = 600, y = 220)
        lbl5 = Label(self.frame, text = 'Filtered amps:', foreground="white")
        lbl5.place(x = 600, y = 270)
        lbl6 = Label(self.frame, text = 'Experimental data:', foreground="white")
        lbl6.place(x = 600, y = 50)
        lbl7 = Label(self.frame, text = 'Execution setup data:')
        lbl7.place(x = 130, y = 0)
        lbl8 = Label(self.frame, text = 'Velocity [rad/s]:')
        lbl8.place(x = 130, y = 70)
        lbl9 = Label(self.frame, text = 'Torque [%]:')
        lbl9.place(x = 130, y = 110)
        lbl10 = Label(self.frame, text = 'Position [rad]:')
        lbl10.place(x = 130, y = 30)
        lbl11 = Label(self.frame, text = 'Execution mode:')
        lbl11.place(x = 0, y = 0)
        pltlbl3 = Label(self.frame, text = 'Execution sample time [ms]:')
        pltlbl3.place(x = 0, y = 220)
        pltlbl1 = Label(self.frame, text = 'Plot execution time [s]:')
        pltlbl1.place(x = 0, y = 270)
        pltlbl4 = Label(self.frame, text = 'Execution time [s]:')
        pltlbl4.place(x = 0, y = 170)
        #Checkboxes
        #pos mode
        self.varp = IntVar()        
        self.check_p = Checkbutton(self.frame, text = 'Position mode',  variable = self.varp, command = self.posmode)
        self.check_p.place(x = 0, y = 30)
        #vel mode
        self.varv = IntVar()        
        self.check_v = Checkbutton(self.frame, text = 'Velocity mode', variable = self.varv, command = self.velmode)
        self.check_v.place(x = 0, y = 70)
        #torquemode
        self.vart = IntVar()        
        self.check_t = Checkbutton(self.frame, text = 'Torque mode',  variable = self.vart, command = self.torquemode)
        self.check_t.place(x = 0, y = 110)
        #contador
        self.cont = 0
        global m_pos, m_vel, m_tor
        m_pos = list()
        m_vel = list()
        m_tor = list()


    def get_position(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        pos = cia402.GetPosition(); 
        self.position.delete('0', END)
        self.position.insert(0, str(pos)) 
        m_pos.append(pos)

    def get_velocity(self):
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        vel = cia402.GetVelocity();
        self.velocity.delete('0', END)
        self.velocity.insert(0, str(vel))
        m_vel.append(vel)
 
        
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
        m_tor.append(amps)

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
        self.spos['state'] = 'active'
        self.svel['state'] = 'disabled'
        self.stor['state'] = 'disabled'

    def velmode(self):
        self.varp.set(False)
        self.vart.set(False)
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        cia402.Setup_Velocity_Mode();
        self.spos['state'] = 'disabled'
        self.svel['state'] = 'active'
        self.stor['state'] = 'disabled' 

    def torquemode(self):
        self.varv.set(False)
        self.varp.set(False)
        port = porter
        pm1 = SocketCanPort.SocketCanPort("can1")
        cia402 = Cia402device.CiA402Device(port, pm1);
        cia402.Setup_Torque_Mode();
        self.spos['state'] = 'disabled'
        self.svel['state'] = 'disabled'
        self.stor['state'] = 'active'

    def loop(self, toggle=False):
        global tracking_var
        time_lim = self.exec_time.get() #Limite de tiempo
        if int(time_lim) <= int(self.cont):
            tracking_var = False
        else:
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
            global tsamp
            tsamp = self.sample.get()
            frec = int(tsamp)/1000 #Numero de segundos de muestreo
            #Actualizo el contador
            self.cont = self.cont + frec 
            self.frame.after(tsamp, self.loop) #tsamp es el numero de milisegundos que dura el intervalo entre la llamada a la función loop
        else:
            #Acabada la simulación saco la gráfica
            tmeasured = self.time_frame.get()
            #Saco cuantos componentes son:
            nbr_pts = int(tmeasured)/(int(tsamp)/1000)
            final_vec_p = m_pos[-int(nbr_pts):]
            final_vec_v = m_vel[-int(nbr_pts):]

            #Pinto las gráficas
            #Posición
            plt.subplot(311)
            plt.plot(m_pos[:],'b', lw = 1.5) #label hace referencia a la leyenda
            plt.plot(m_pos[:], 'ro') #ro indica r(red)o(circles)
            plt.grid(True)
            plt.ylabel('Position')
            #Velocidad
            plt.subplot(312)
            plt.plot(m_vel[:],'b', lw = 1.5) #label hace referencia a la leyenda
            plt.plot(m_vel[:], 'ro') #ro indica r(red)o(circles)
            plt.grid(True)
            plt.ylabel('Velocity')
            #Amperaje
            plt.subplot(313)
            plt.plot(m_tor[:],'b', lw = 1.5) #label hace referencia a la leyenda
            plt.plot(m_tor[:], 'ro') #ro indica r(red)o(circles)
            plt.grid(True)
            plt.ylabel('Amps')
            plt.xlabel('Sample measure point')
            #pinto
            plt.show()

class Window3(Cia402device.CiA402Device):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Style = Style()
        self.Style.theme_use('default')
        self.master.title('Teo´s error window')
        self.master.geometry('820x450+100+150')
        self.frame.pack(fill = BOTH, expand = 1)
        #Quit
        self.quitButton = Button(self.frame, text = 'Quit error window', command = self.master.destroy)
        self.quitButton.place(x = 600, y = 350)
        #Get Msg
        self.gmsg = Button(self.frame,text = 'Get error message', command = lambda : self.loop_msg(True))
        self.gmsg.place(x = 600, y = 300)
        #Labels 
        lbl1 = Label(self.frame, text = 'Messages:')
        lbl1.place(x = 10, y = 10)
        lbl4 = Label(self.frame, text = 'Error description:')
        lbl4.place(x = 410, y = 10)
        lbl6 = Label(self.frame, text = 'Filter messages by first number:')
        lbl6.place(x = 410, y = 30)
        #textboxes
        self.canid = Text(self.frame, width = 48)
        self.canid.place(x = 10, y = 30, height = 220)
        self.err_typ = Text(self.frame, width = 48)
        self.err_typ.place(x = 410, y = 30, height = 220)
        #Checkboxes
        # error, 0
        self.var0 = IntVar()        
        self.check_0 = Checkbutton(self.frame, text = '0, Error Reset or no error.',  variable = self.var0)
        self.check_0.place(x = 10, y = 260)
        # error, 1
        self.var1 = IntVar()        
        self.check_1 = Checkbutton(self.frame, text = '1, Generic error.', variable = self.var1)
        self.check_1.place(x = 10, y = 290)
        # error, 2
        self.var2 = IntVar()        
        self.check_2 = Checkbutton(self.frame, text = '2, Current messages.',  variable = self.var2)
        self.check_2.place(x = 10, y = 320)
        # error, 3
        self.var3 = IntVar()        
        self.check_3 = Checkbutton(self.frame, text = '3, Voltage messages.',  variable = self.var3)
        self.check_3.place(x = 10, y = 350)
        # error, 4
        self.var4 = IntVar()        
        self.check_4 = Checkbutton(self.frame, text = '4, Temperature messages.', variable = self.var4)
        self.check_4.place(x = 10, y = 380)
        # error, 5
        self.var5 = IntVar()        
        self.check_5 = Checkbutton(self.frame, text = '5, Device software messages.',  variable = self.var5)
        self.check_5.place(x = 250, y = 260)
        # error, 6
        self.var6 = IntVar()        
        self.check_6 = Checkbutton(self.frame, text = '6, Device hardware messages.', variable = self.var6)
        self.check_6.place(x = 250, y = 290)
        # error, 7
        self.var7 = IntVar()        
        self.check_7 = Checkbutton(self.frame, text = '7, Additional modules messages',  variable = self.var7)
        self.check_7.place(x = 250, y = 320)
        # error, 8
        self.var8 = IntVar()        
        self.check_8 = Checkbutton(self.frame, text = '8, Monitoring messages.',  variable = self.var8)
        self.check_8.place(x = 250, y = 350)
        # error, 9
        self.var9 = IntVar()        
        self.check_9 = Checkbutton(self.frame, text = '9, External error messages.', variable = self.var9)
        self.check_9.place(x = 250, y = 380)
        #error, F
        self.varF = IntVar()        
        self.check_F = Checkbutton(self.frame, text = 'F, Device specific messages.',  variable = self.varF)
        self.check_F.place(x = 250, y = 410)

        global pm1
        pm1 = SocketCanPort.SocketCanPort("can1")
        filtered = False


    def getmsg(self):
        #Obtengo lo nuevo
        err,cid,dat,siz = pm1.GetMsg()
        lister = self.checkbox_check()
        if not lister:
            if int(siz) < 4:
                msg = 'Cid: ' + str(hex(cid)) + ', Data: ' + str(hex(dat)) + ', Size: ' +str(siz)
                self.canid.insert(END, msg + '\n')
                #print(str(hex(cid))[2])
                warning = self.warning_generator(str(hex(cid))[2])
                self.err_typ.insert(END, warning + '\n')




        else:
            #Inserto lo nuevo solo si está marcado:
            for i in range(0,len(lister)):
                if str(lister[i]) == str(hex(cid))[2]:
                    filtered = True
                    break
                else:
                    filtered = False
            if filtered == True:
                if int(siz) < 4:
                    msg = 'Cid: ' + str(hex(cid)) + ', Data: ' + str(hex(dat)) + ', Size: ' +str(siz)
                    self.canid.insert(END, msg + '\n')
                    warning = self.warning_generator(str(hex(cid))[2])
                    self.err_typ.insert(END, warning + '\n')



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

    def warning_generator(self, varx):
        if varx == '0':
            msgg = 'Error reset or no error'
        elif varx == '1':
            msgg = 'Generic error'
        elif varx == '2':
            msgg = 'Current warning'
        elif varx == '3':
            msgg = 'Voltage warning'
        elif varx == '4':
            msgg = 'Temperature warning'
        elif varx == '5':
            msgg = 'Device hardware warning'
        elif varx == '6':
            msgg = 'Device software warning'
        elif varx == '7':
            msgg = 'Additional modules warning'
        elif varx == '8':
            msgg = 'Monitoring warning'
        elif varx == '9':
            msgg = 'Additional functions warning'
        elif varx == 'F':
            msgg = 'Device specific warning'
        return msgg








def main(): 
    root = tk.Tk() 
    app = Master_Window(root)
    root.mainloop()


tracking_var = False
main()
