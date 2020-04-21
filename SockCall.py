from ctypes import cdll


lib = cdll.LoadLibrary('./CiA402Device/libSocket.so')

class Socket:
    def SocketCan():
        lib.SocketCanPort()
Socker = Socket()
Socker.SocketCanPort()




