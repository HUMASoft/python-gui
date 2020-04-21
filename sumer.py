from ctypes import *

lib = cdll.LoadLibrary('./API/libhell.so')

'La función dentro del script llamada suma tiene variables a y b de tipo int'

'Quiero que a valga 2 y b valga 3, los declaro:'
a = c_int(2)
b = c_int(3)


class h_cl:
    def helou():
        lib.main()
hl = h_cl
hl.helou()
