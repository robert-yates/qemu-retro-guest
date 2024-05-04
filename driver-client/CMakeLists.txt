cmake_minimum_required(VERSION 3.14)

project(DriverClient C)


add_library(${PROJECT_NAME} STATIC  src/fxhook.c
                                    src/fxhpat.c
                                    src/fxlib9x.c
                                    src/fxlibnt.c
                                    src/fxtime.c
                                    src/md5.c
)

include_directories("./inc")
target_include_directories(${PROJECT_NAME} PUBLIC ./inc)