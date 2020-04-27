
from distutils.core import setup, Extension

name = "CiA301CommPort"
version = "1.0"

example_module = Extension('_CiA301CommPort', sources=['CiA301CommPort.cpp', 'CiA301CommPort.i'], extra_objects = ['_PortBase.so'], runtime_library_dirs = ['./'], swig_opts=['-Isrc', '-c++'])

setup(name = name, ext_modules = [example_module])

