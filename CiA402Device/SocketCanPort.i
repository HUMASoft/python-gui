/* SocketCanPort.i */
%module SocketCanPort
%include <std_string.i>
%include "stdint.i"
%include "typemaps.i"
%import "PortBase.i"
%ignore SocketCanPort();
%apply unsigned int *INOUT { UInt32 };

%{
#define SWIG_FILE_WITH_INIT
#include "SocketCanPort.h"
%}


    
%include "SocketCanPort.h"


