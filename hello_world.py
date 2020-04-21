from ctypes import *

lib = cdll.LoadLibrary('./API/libhell.so')

lib.main()
