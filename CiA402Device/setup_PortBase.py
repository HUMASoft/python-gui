
from distutils.core import setup, Extension

name = "PortBase"
version = "1.0"

example_module = Extension('_PortBase', sources=['PortBase.cpp','PortBase.i'], swig_opts=['-builtin', '-c++'])

setup(name = name, ext_modules = [example_module])
