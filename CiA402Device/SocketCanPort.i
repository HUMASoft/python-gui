/* SocketCanPort.i */
%module SocketCanPort
%include <std_string.i>
%include "stdint.i"
%include "typemaps.i"
%import "PortBase.i"
%ignore SocketCanPort();
typedef unsigned int __uint32_t;
long GetMsg(uint32_t *OUTPUT, uint8_t *OUTPUT, uint8_t *OUTPUT);
%{
#define SWIG_FILE_WITH_INIT
#include "SocketCanPort.h"
%}



%include "SocketCanPort.h"


