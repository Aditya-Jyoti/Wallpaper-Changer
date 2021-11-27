cmake_minimum_required(VERSION 3.1)

project(Wallpaper_Changer VERSION 1.0
                          DESCRIPTION "A program that automatically changes windows wallpaper"
                          LANGUAGES CXX)

include(FetchContent)
FetchContent_Declare(cpr GIT_REPOSITORY https://github.com/libcpr/cpr.git GIT_TAG 67e12da316754ff3c6c91b50aafb2658438f3c1e)
FetchContent_MakeAvailable(cpr)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE cpr::cpr)