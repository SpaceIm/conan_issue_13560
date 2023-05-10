cmake_minimum_required(VERSION 3.15)
project(libC_issue13560 LANGUAGES CXX)

find_package(libb_issue13560 REQUIRED CONFIG)

add_library(libC_issue13560 libC_issue13560.cpp)
target_link_libraries(libC_issue13560 PRIVATE libb_issue13560::libb_issue13560)

add_executable(execC_issue_13560 execC_issue13560.cpp)
target_link_libraries(execC_issue_13560 PRIVATE libC_issue13560)

include(GNUInstallDirs)
install(FILES libC_issue13560.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(
    TARGETS libC_issue13560 execC_issue_13560
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
