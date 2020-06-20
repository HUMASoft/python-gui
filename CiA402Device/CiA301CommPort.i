/* CiA301CommPort.i */
%module CiA301CommPort
%include <std_string.i>
%include "stdint.i"
%include "typemaps.i"
%import "PortBase.i"


%{
#define SWIG_FILE_WITH_INIT
#include "CiA301CommPort.h"
%}

%ignore  ReadSDO(vector<uint8_t> address, int subindex);
    
%include "CiA301CommPort.h"




