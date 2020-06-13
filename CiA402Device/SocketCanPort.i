/* SocketCanPort.i */
%module SocketCanPort
%include <std_string.i>
%include "stdint.i"
%include "typemaps.i"
typedef unsigned int __uint32_t;

%import "PortBase.i"
%ignore SocketCanPort();



%{
#define SWIG_FILE_WITH_INIT
#include "SocketCanPort.h"
%}



%include "SocketCanPort.h"


