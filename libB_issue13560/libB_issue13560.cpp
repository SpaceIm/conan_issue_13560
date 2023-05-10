#include "libB_issue13560.h"

#include <libA_issue13560.h>

#include <iostream>

namespace libB_issue13560 {

void libB_issue13560_function() {
    std::cout << "libB_issue13560_function called" << std::endl;
    libA_issue13560::libA_issue13560_function();
}

}
