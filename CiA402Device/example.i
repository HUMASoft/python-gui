/* hw.i */
%module example
%include <std_string.i>
%include "stdint.i"
%include "typemaps.i"
%apply uint32_t &OUTPUT { uint32_t &result};
%apply uint8_t *OUTPUT { uint8_t *a};
%apply uint8_t *OUTPUT { uint8_t *b};


%{
#define SWIG_FILE_WITH_INIT
#include "example.h"
%}

%include "example.h"

