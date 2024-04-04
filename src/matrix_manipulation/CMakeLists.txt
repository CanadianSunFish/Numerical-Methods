cmake_minimum_required(VERSION 3.27)
project(m5600)

set(CMAKE_CXX_STANDARD 17)

add_executable(m5600 gaussElim.cpp
        decompositionLU.cpp
)
