cmake_minimum_required(VERSION 3.14)
project(LibB)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

set(LIB_HEADERS "include/libB.h")
set(LIB_SOURCES "src/libB.cpp")
set(STATIC_LIB_NAME ${PROJECT_NAME})

add_library(${STATIC_LIB_NAME} STATIC)
target_include_directories(${STATIC_LIB_NAME} PUBLIC "include")
target_sources(${STATIC_LIB_NAME} PRIVATE ${LIB_SOURCES} PUBLIC ${LIB_HEADERS})