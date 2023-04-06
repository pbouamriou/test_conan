cmake_minimum_required(VERSION 3.14)
project(exeC)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

set(EXE_SOURCES "src/main.cpp")
set(EXE_NAME ${PROJECT_NAME})

find_package(LibA)

# Executable (static)
add_executable(${EXE_NAME} ${EXE_SOURCES})
target_link_libraries(${EXE_NAME} LibA::LibA)