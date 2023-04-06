from conans import ConanFile, CMake

class BuildLibB(ConanFile):
    name = "LibB"
    version = "1.0.2"

    settings = "os", "compiler", "build_type", "arch"
    license = "None"
    url = "None"
    description = "LibB"
    generators = "cmake_paths", "cmake_find_package"
    exports_sources = "include/*", "src/*", "CMakeLists.txt"


    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        self.copy("*.h", src="include", dst="include")
        self.copy("*.a", src="", dst="lib")
        self.copy("*.lib", src="", dst="lib")

    def package_info(self):
        self.cpp_info.includesdirs = ["include/libb"]
        self.cpp_info.libs = ["libb"]