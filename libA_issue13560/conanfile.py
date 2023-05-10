import os

from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import rmdir


class LibA_issue13560(ConanFile):
    name = "liba_issue13560"
    version = "1.0.0"
    package_type = "library"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "cmakedeps": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "cmakedeps": True,
    }

    exports_sources = "CMakeLists.txt", "*.cpp", "*.h", "*.cmake.in"
    generators = "CMakeToolchain"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        self.options["*"].cmakedeps = self.options.cmakedeps

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        if self.options.cmakedeps:
            rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))

    def package_info(self):
        self.cpp_info.libs = ["libA_issue13560"]
        if self.options.cmakedeps:
            self.cpp_info.set_property("cmake_file_name", "libA_issue13560")
            self.cpp_info.set_property("cmake_target_name", "libA_issue13560::libA_issue13560")
        else:
            self.cpp_info.set_property("cmake_find_mode", "none")
            self.cpp_info.builddirs.append(os.path.join("lib", "cmake", "libA_issue13560"))
