cmake_minimum_required(VERSION 3.15)
project(libC_issue13560 VERSION 1.0.0 LANGUAGES CXX)

find_package(libB_issue13560 REQUIRED CONFIG)

add_library(libC_issue13560 libC_issue13560.cpp)
set_target_properties(libC_issue13560 PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
target_link_libraries(libC_issue13560 PRIVATE libB_issue13560::libB_issue13560)

add_executable(execC_issue_13560 execC_issue13560.cpp)
target_link_libraries(execC_issue_13560 PRIVATE libC_issue13560)

include(GNUInstallDirs)
install(FILES libC_issue13560.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(
    TARGETS libC_issue13560 execC_issue_13560
    EXPORT libC_issue13560Export
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

include(CMakePackageConfigHelpers)
configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/libC_issue13560Config.cmake.in
    libC_issue13560Config.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/libC_issue13560
)

write_basic_package_version_file(
    libC_issue13560ConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

export(
    EXPORT libC_issue13560Export
    NAMESPACE libC_issue13560::
    FILE libC_issue13560Targets.cmake
)

install(
    EXPORT libC_issue13560Export
    NAMESPACE libC_issue13560::
    FILE libC_issue13560Targets.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/libC_issue13560
)

install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/libC_issue13560Config.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/libC_issue13560ConfigVersion.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/libC_issue13560
)
