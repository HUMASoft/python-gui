from distutils.core import setup, Extension

name = "SocketCanPort"
version = "1.0"

example_module = Extension('_SocketCanPort', sources=['SocketCanPort.cpp','SocketCanPort.i'],extra_objects = ['_PortBase.so'], runtime_library_dirs = ['./'] ,swig_opts=['-Isrc','-c++'])

setup(name = name, ext_modules = [example_module])
