
from distutils.core import setup, Extension

name = "Cia402device"
version = "1.0"

example_module = Extension('_Cia402device', sources=['Cia402device.cpp','Cia402device.i'],extra_objects = ['_PortBase.cpython-36m-x86_64-linux-gnu.so', '_CiA402SetupData.cpython-36m-x86_64-linux-gnu.so', '_CiA301CommPort.cpython-36m-x86_64-linux-gnu.so'], runtime_library_dirs = ['/home/jorgevi8/python-gui/CiA402Device/'] ,swig_opts=['-Isrc','-c++'])

setup(name = name, ext_modules = [example_module])
