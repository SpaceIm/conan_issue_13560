cmake_minimum_required(VERSION 3.15)
project(libB_issue13560 LANGUAGES CXX)

find_package(liba_issue13560 REQUIRED CONFIG)

add_library(libB_issue13560 libB_issue13560.cpp)
target_link_libraries(libB_issue13560 PRIVATE liba_issue13560::liba_issue13560)

include(GNUInstallDirs)
install(FILES libB_issue13560.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(
    TARGETS libB_issue13560
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
