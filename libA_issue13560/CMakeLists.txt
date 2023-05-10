cmake_minimum_required(VERSION 3.15)
project(libA_issue13560 VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_VERBOSE_MAKEFILE ON)

add_library(libA_issue13560 libA_issue13560.cpp)
set_target_properties(libA_issue13560 PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)

include(GNUInstallDirs)
install(FILES libA_issue13560.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(
    TARGETS libA_issue13560
    EXPORT libA_issue13560Export
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

include(CMakePackageConfigHelpers)
configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/libA_issue13560Config.cmake.in
    libA_issue13560Config.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/libA_issue13560
)

write_basic_package_version_file(
    libA_issue13560ConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

export(
    EXPORT libA_issue13560Export
    NAMESPACE libA_issue13560::
    FILE libA_issue13560Targets.cmake
)

install(
    EXPORT libA_issue13560Export
    NAMESPACE libA_issue13560::
    FILE libA_issue13560Targets.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/libA_issue13560
)

install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/libA_issue13560Config.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/libA_issue13560ConfigVersion.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/libA_issue13560
)
