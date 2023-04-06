from conans import ConanFile, CMake
import os, shutil


class BuildExeC(ConanFile):
    name = "ExeC"
    version = "1.0.0"

    settings = "os", "compiler", "build_type", "arch"
    license = "None"
    url = "None"
    description = "ExeC"
    generators = "cmake_paths", "cmake_find_package"
    exports_sources = "include/*", "src/*", "CMakeLists.txt"

    def generate(self):
        for require, dependency in self.dependencies.items():
            self.output.info("Dependency is direct={}: {}".format(require.direct, dependency.ref))

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure(source_folder=".")
        cmake.build()

    def requirements(self):
        self.requires("LibA/[>=1.0 <2.0]")
        self.requires("LibB/1.0.1", override=True)

    def package_id(self):
        self.info.requires["LibA"].semver_direct_mode()
        self.info.requires["LibB"].semver_mode() # Pourtant elle est transitive (donc non nécessaire)

    def package(self):
        self.copy("*.h", src="include", dst="include")
        self.copy("ExeC", src="", dst="bin")