#include "libB.h"

#include <iostream>

extern "C" void display2() {
    std::cout << "display2 called !!!" << std::endl;
    std::cout << "display2 is better now" << std::endl;
    std::cout << "display2 is extremly better now" << std::endl;
}