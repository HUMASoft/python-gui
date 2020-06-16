/* SocketCanPort.i */
%module SocketCanPort
%include "stdint.i"
%include <std_string.i>
%include "typemaps.i"
%import "PortBase.i"
%ignore SocketCanPort();
%apply uint32_t &OUTPUT { uint32_t &canId};
%apply uint8_t *OUTPUT { uint8_t *data};
%apply uint8_t &OUTPUT { uint8_t &size};


%{
#define SWIG_FILE_WITH_INIT
#include "SocketCanPort.h"
%}



%include "SocketCanPort.h"


