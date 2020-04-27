
from distutils.core import setup, Extension

name = "CiA301CommPort"
version = "1.0"

example_module = Extension('_CiA301CommPort', sources=['CiA301CommPort.cpp', 'CiA301CommPort.i'], extra_objects = ['_PortBase.cpython-36m-x86_64-linux-gnu.so'], runtime_library_dirs = ['/home/jorgevi8/python-gui/CiA402Device/'], swig_opts=['-Isrc', '-c++'])

setup(name = name, ext_modules = [example_module])

