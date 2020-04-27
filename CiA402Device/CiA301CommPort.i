/* CiA301CommPort.i */
%module CiA301CommPort
%import "PortBase.i"
%ignore tx0;
%ignore rx0;

%{
#define SWIG_FILE_WITH_INIT
#include "CiA301CommPort.h"
%}

%ignore  ReadSDO(vector<uint8_t> address, int subindex);
    
%include "CiA301CommPort.h"




