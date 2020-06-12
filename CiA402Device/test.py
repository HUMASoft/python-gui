from distutils.core import setup, Extension

setup(name="example", py_modules=['example'], ext_modules=[Extension("_example", ["test.i","test.cpp"], swig_opts=['-c++'], extra_compile_args=['--std=c++11'])])