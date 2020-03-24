from ctypes import cdll
lib = cdll.LoadLibrary('./API/libfoo.so')
class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()
    def bar(self):
        lib.Foo_bar(self.obj)
f = Foo()
import tkinter as tk
#Se organizan los widgets con el frame
class App(tk.Frame): #Creo una subclase dentro del frame del tkinter

    def __init__(self, master): #self es la forma de referirse a los atributos de la clase
        self.master = master
        self.entry1 = tk.Entry(self.master, width=5)
        self.entry1.grid(row=1, column=0)
        #Labels en GUI
        self.lbl1 = tk.Label(self.master, text = "Do you want to display the hello message?")
        self.lbl1.grid(row = 0, column = 0)
       #Meto el botón
        btn1 = tk.Button(self.master, text = "Button", command=self.show_msg)
        btn1.grid(row = 2, column = 0)
    def show_msg(self):
        msg = self.entry1.get()
        if msg == 'yes':
            f.bar()
if __name__ == "__main__":
    root = tk.Tk()
    myapp = App(root)
    root.mainloop()
