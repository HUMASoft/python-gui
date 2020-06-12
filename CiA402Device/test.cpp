#include "test.h"

#include <iostream>

int func(uint8_t* a, const size_t len) {
  int result = 0;
  for (size_t i = 0 ; i < len ; i++) {
    result += int(a[i]);
  }
  return result;
}