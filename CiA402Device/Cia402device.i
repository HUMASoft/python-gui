/* Cia402device.i */
%module Cia402device
%import "PortBase.i"
%import "CiA301CommPort.i" /*Clase base*/
%import "CiA402SetupData.i"

%{
#define SWIG_FILE_WITH_INIT
#include "Cia402device.h"
%}


%include "Cia402device.h"
