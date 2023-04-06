from conans import ConanFile, CMake

class BuildLibA(ConanFile):
    name = "LibA"
    version = "1.0.0"

    settings = "os", "compiler", "build_type", "arch"
    license = "None"
    url = "None"
    description = "LibA"
    generators = "cmake_paths", "cmake_find_package"
    exports_sources = "include/*", "src/*", "CMakeLists.txt"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def requirements(self):
        self.requires("LibB/[>=1.0 <2.0]@")

    def package_id(self):
        self.info.requires["LibB"].semver_direct_mode()

    def package(self):
        self.copy("*.h", src="include", dst="include")
        self.copy("*.a", src="", dst="lib")
        self.copy("*.lib", src="", dst="lib")

    def package_info(self):
        self.cpp_info.includesdirs = ["include/liba"]
        self.cpp_info.libs = ["liba"]