
from distutils.core import setup, Extension

name = "CiA402SetupData"
version = "1.0"

example_module = Extension('_CiA402SetupData', sources=['CiA402SetupData.cpp', 'CiA402SetupData.i'], swig_opts=['-Isrc', '-c++'])

setup(name = name, ext_modules = [example_module])

