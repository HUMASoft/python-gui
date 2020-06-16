# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_PortBase')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_PortBase')
    _PortBase = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_PortBase', [dirname(__file__)])
        except ImportError:
            import _PortBase
            return _PortBase
        try:
            _mod = imp.load_module('_PortBase', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _PortBase = swig_import_helper()
    del swig_import_helper
else:
    import _PortBase
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class PortBase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PortBase, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PortBase, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def getPortId(self):
        return _PortBase.PortBase_getPortId(self)

    def FlushMsg(self):
        return _PortBase.PortBase_FlushMsg(self)

    def SetFilter(self, canId, mask):
        return _PortBase.PortBase_SetFilter(self, canId, mask)

    def GetMsg(self, canId, data, size):
        return _PortBase.PortBase_GetMsg(self, canId, data, size)

    def PutMsg(self, canId, data, size):
        return _PortBase.PortBase_PutMsg(self, canId, data, size)

    def GetNMT(self, data, size):
        return _PortBase.PortBase_GetNMT(self, data, size)
    __swig_destroy__ = _PortBase.delete_PortBase
    __del__ = lambda self: None
PortBase_swigregister = _PortBase.PortBase_swigregister
PortBase_swigregister(PortBase)

# This file is compatible with both classic and new-style classes.


