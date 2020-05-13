/* SocketCanPort.i */
%module SocketCanPort
%include <std_string.i>
%include "typemaps.i"
%import "PortBase.i"
%ignore SocketCanPort();


%{
#define SWIG_FILE_WITH_INIT
#include "SocketCanPort.h"
%}


    
%include "SocketCanPort.h"


