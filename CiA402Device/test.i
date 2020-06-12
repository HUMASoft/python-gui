%module example
%{
  #include "test.h"
%}

%include "carrays.i"
%include "stdint.i"
%array_functions(uint8_t, uint8Array);

%include "test.h"