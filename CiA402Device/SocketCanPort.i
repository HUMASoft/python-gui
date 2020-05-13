/* CiA301CommPort.i */
%module SocketCanPort
%import "PortBase.i"
%ignore tx0;
%ignore rx0;

%{
#define SWIG_FILE_WITH_INIT
#include "SocketCanPort.h"
%}


    
%include "SocketCanPort.h"


