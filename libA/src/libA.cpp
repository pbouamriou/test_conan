#include "libB.h"

#include <iostream>

extern "C" void display() {
    std::cout << "display called !!!" << std::endl;
    display2();
}