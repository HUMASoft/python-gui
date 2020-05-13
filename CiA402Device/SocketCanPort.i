/* SocketCanPort.i */
%module SocketCanPort
%import "PortBase.i"
%ignore SocketCanPort();
%include "typemaps.i"

%{
#define SWIG_FILE_WITH_INIT
#include "SocketCanPort.h"
%}


    
%include "SocketCanPort.h"


