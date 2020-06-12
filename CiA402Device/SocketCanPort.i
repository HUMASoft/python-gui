/* SocketCanPort.i */
%module SocketCanPort
%include <std_string.i>
%include "stdint.i"
%include "typemaps.i"
%import "PortBase.i"
%ignore SocketCanPort();

%{
#define SWIG_FILE_WITH_INIT
#include "SocketCanPort.h"
%}

%inline %{
extern long GetMsg(unsigned int *OUTPUT, unsigned int *OUTPUT, unsigned int *OUTPUT);
%}

%include "SocketCanPort.h"


