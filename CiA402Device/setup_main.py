from distutils.core import setup, Extension

name = "move_motor"
version = "1.0"

example_module = Extension('_main', sources=['move_motor.cpp','move_motor.i'],extra_objects = ['_SocketCanPort.so', '_Cia402device.so', '_CiA301CommPort.so'], runtime_library_dirs = ['./'] ,swig_opts=['-Isrc','-c++'])

setup(name = name, ext_modules = [example_module])
