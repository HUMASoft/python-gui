/* CiA301CommPort.i */
%module SocketCanPort
%import "PortBase.i"
%ignore SocketCanPort.SocketCanPort();

%{
#define SWIG_FILE_WITH_INIT
#include "SocketCanPort.h"
%}


    
%include "SocketCanPort.h"


