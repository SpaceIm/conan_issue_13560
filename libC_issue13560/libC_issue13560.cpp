#include "libC_issue13560.h"

#include <libB_issue13560.h>

#include <iostream>

namespace libC_issue13560 {

void libC_issue13560_function() {
    std::cout << "libC_issue13560_function called" << std::endl;
    libB_issue13560::libB_issue13560_function();
}

}
