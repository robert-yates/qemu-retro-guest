cmake_minimum_required(VERSION 3.14)

project(DriverClient C)


add_library(${PROJECT_NAME} STATIC  src/fxhook.c
                                    src/fxhpat.c
                                    src/fxlib9x.c
                                    src/fxlibnt.c
                                    src/fxtime.c
                                    src/md5.c
)
target_compile_options(${PROJECT_NAME} PRIVATE "-march=x86-64-v2" "-mtune=generic" "-O3" "-pipe" "-Wall" "-Werror" "-flto" "-fomit-frame-pointer")
target_link_options(${PROJECT_NAME} PRIVATE "-static-libgcc" "-static-libstdc++" "-static")
include_directories("./inc")
target_include_directories(${PROJECT_NAME} PUBLIC ./inc)