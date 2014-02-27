set(EXECUTABLE_OUTPUT_PATH bin)
set(CMAKE_BUILD_TYPE Debug)

cmake_minimum_required(VERSION 2.8)
project(sobel)
find_package(OpenCV REQUIRED)

add_executable(sobel sobel.cpp)
add_executable(orientation gradient-orientation/new-orien.cpp)

target_link_libraries(sobel ${OpenCV_LIBS})
target_link_libraries(orientation ${OpenCV_LIBS})
