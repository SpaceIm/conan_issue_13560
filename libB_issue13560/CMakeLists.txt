cmake_minimum_required(VERSION 3.15)
project(libB_issue13560 VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_VERBOSE_MAKEFILE ON)

find_package(libA_issue13560 REQUIRED CONFIG)

add_library(libB_issue13560 libB_issue13560.cpp)
set_target_properties(libB_issue13560 PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
target_link_libraries(libB_issue13560 PRIVATE libA_issue13560::libA_issue13560)

include(GNUInstallDirs)
install(FILES libB_issue13560.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(
    TARGETS libB_issue13560
    EXPORT libB_issue13560Export
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

include(CMakePackageConfigHelpers)
configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/libB_issue13560Config.cmake.in
    libB_issue13560Config.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/libB_issue13560
)

write_basic_package_version_file(
    libB_issue13560ConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

export(
    EXPORT libB_issue13560Export
    NAMESPACE libB_issue13560::
    FILE libB_issue13560Targets.cmake
)

install(
    EXPORT libB_issue13560Export
    NAMESPACE libB_issue13560::
    FILE libB_issue13560Targets.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/libB_issue13560
)

install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/libB_issue13560Config.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/libB_issue13560ConfigVersion.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/libB_issue13560
)
