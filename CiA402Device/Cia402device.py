# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Cia402device
else:
    import _Cia402device

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import PortBase
import CiA301CommPort
import CiA402SetupData
PI = _Cia402device.PI
RPM2RADS = _Cia402device.RPM2RADS
RADS2RPM = _Cia402device.RADS2RPM
DEG2RADS = _Cia402device.DEG2RADS
RADS2DEG = _Cia402device.RADS2DEG
HIGHPART_BITSHIFT_16 = _Cia402device.HIGHPART_BITSHIFT_16
ANALOGUE_INPUT_SCALE = _Cia402device.ANALOGUE_INPUT_SCALE
class CiA402Device(CiA301CommPort.CiA301CommPort):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Cia402device.CiA402Device_swiginit(self, _Cia402device.new_CiA402Device(*args))

    def CheckStatus(self):
        return _Cia402device.CiA402Device_CheckStatus(self)

    def PrintStatus(self):
        return _Cia402device.CiA402Device_PrintStatus(self)

    def SwitchOn(self):
        return _Cia402device.CiA402Device_SwitchOn(self)

    def SwitchOff(self):
        return _Cia402device.CiA402Device_SwitchOff(self)

    def QuickStop(self):
        return _Cia402device.CiA402Device_QuickStop(self)

    def GetPosition(self):
        return _Cia402device.CiA402Device_GetPosition(self)

    def GetVelocity(self):
        return _Cia402device.CiA402Device_GetVelocity(self)

    def GetFilteredVelocity(self, samples):
        return _Cia402device.CiA402Device_GetFilteredVelocity(self, samples)

    def GetMeanVelocity(self):
        return _Cia402device.CiA402Device_GetMeanVelocity(self)

    def GetAmps(self):
        return _Cia402device.CiA402Device_GetAmps(self)

    def GetFilterdAmps(self):
        return _Cia402device.CiA402Device_GetFilterdAmps(self)

    def SetCommunications(self, fdPort):
        return _Cia402device.CiA402Device_SetCommunications(self, fdPort)

    def CheckError(self):
        return _Cia402device.CiA402Device_CheckError(self)

    def OperationMode(self, new_mode):
        return _Cia402device.CiA402Device_OperationMode(self, new_mode)

    def Setup_Velocity_Mode(self, acceleration=1, target=0):
        return _Cia402device.CiA402Device_Setup_Velocity_Mode(self, acceleration, target)

    def Setup_Torque_Mode(self):
        return _Cia402device.CiA402Device_Setup_Torque_Mode(self)

    def SetTorque(self, target):
        return _Cia402device.CiA402Device_SetTorque(self, target)

    def SetAmpRaw(self, target):
        return _Cia402device.CiA402Device_SetAmpRaw(self, target)

    def ForceSwitchOff(self):
        return _Cia402device.CiA402Device_ForceSwitchOff(self)

    def SetPosition(self, target):
        return _Cia402device.CiA402Device_SetPosition(self, target)

    def SetupPositionMode(self, velocity=1, acceleration=1):
        return _Cia402device.CiA402Device_SetupPositionMode(self, velocity, acceleration)

    def SetPositionRECURSIVE_test(self, target):
        return _Cia402device.CiA402Device_SetPositionRECURSIVE_test(self, target)

    def SetTarget_VELOCITY_PROPORCIONAL(self, target, kp):
        return _Cia402device.CiA402Device_SetTarget_VELOCITY_PROPORCIONAL(self, target, kp)

    def Reset(self):
        return _Cia402device.CiA402Device_Reset(self)

    def StartNode(self):
        return _Cia402device.CiA402Device_StartNode(self)

    def SetVelocity(self, target):
        return _Cia402device.CiA402Device_SetVelocity(self, target)

    def SetEnc_res(self, lines):
        return _Cia402device.CiA402Device_SetEnc_res(self, lines)

    def SetRed_Mot(self, reduction_ratio):
        return _Cia402device.CiA402Device_SetRed_Mot(self, reduction_ratio)

    def SetSampling_period(self, sampling_period):
        return _Cia402device.CiA402Device_SetSampling_period(self, sampling_period)

    def Scaling(self):
        return _Cia402device.CiA402Device_Scaling(self)
    __swig_destroy__ = _Cia402device.delete_CiA402Device

# Register CiA402Device in _Cia402device:
_Cia402device.CiA402Device_swigregister(CiA402Device)


