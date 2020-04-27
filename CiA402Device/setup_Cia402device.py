
from distutils.core import setup, Extension

name = "Cia402device"
version = "1.0"

example_module = Extension('_Cia402device', sources=['Cia402device.cpp','Cia402device.i'],extra_objects = ['_PortBase.so', '_CiA402SetupData.so', '_CiA301CommPort.so'], runtime_library_dirs = ['./'] ,swig_opts=['-Isrc','-c++'])

setup(name = name, ext_modules = [example_module])
