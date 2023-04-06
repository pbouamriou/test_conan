cmake_minimum_required(VERSION 3.14)
project(LibA)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(LibB)

set(LIB_HEADERS "include/libA.h")
set(LIB_SOURCES "src/libA.cpp")
set(STATIC_LIB_NAME ${PROJECT_NAME})

add_library(${STATIC_LIB_NAME} STATIC)
target_include_directories(${STATIC_LIB_NAME} PUBLIC "include")
target_sources(${STATIC_LIB_NAME} PRIVATE ${LIB_SOURCES} PUBLIC ${LIB_HEADERS})
target_link_libraries(${STATIC_LIB_NAME} LibB::LibB)