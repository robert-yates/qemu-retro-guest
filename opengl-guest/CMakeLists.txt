cmake_minimum_required(VERSION 3.14)

project(opengl C)


add_library(OpenGLIntermediate SHARED   src/szdata.c
                                        src/wrapgl32.c
)
target_compile_options(OpenGLIntermediate PRIVATE "-march=x86-64-v2" "-mtune=generic" "-O3" "-pipe" "-Wall" "-Werror" "-flto" "-fomit-frame-pointer")
target_link_options(OpenGLIntermediate PRIVATE "-static-libgcc" "-static-libstdc++" "-static" "-Wl,-Bstatic,--disable-auto-image-base,--no-seh,--dynamicbase,--nxcompat")
target_link_libraries(OpenGLIntermediate PRIVATE DriverClient)
set_target_properties(OpenGLIntermediate PROPERTIES
    OUTPUT_NAME "opengl32"
    PREFIX ""
)

add_custom_command(
    OUTPUT ${PROJECT_BINARY_DIR}/opengl32.def
    COMMAND gendef - $<TARGET_FILE:OpenGLIntermediate> > ${PROJECT_BINARY_DIR}/opengl32-01.txt
    COMMAND python3  ${PROJECT_SOURCE_DIR}/../scripts/create-def.py ${PROJECT_BINARY_DIR}/opengl32-01.txt > ${PROJECT_BINARY_DIR}/opengl32.def
    DEPENDS OpenGLIntermediate
    COMMENT "Generating .def file from the DLL"
)

add_custom_target(GenerateDEF DEPENDS ${PROJECT_BINARY_DIR}/opengl32.def)

add_library(OpenGLFinal SHARED   src/szdata.c
                                 src/wrapgl32.c
)
target_compile_options(OpenGLFinal PRIVATE "-march=x86-64-v2" "-mtune=generic" "-O3" "-pipe" "-Wall" "-Werror" "-flto" "-fomit-frame-pointer")
set_target_properties(OpenGLFinal PROPERTIES
    OUTPUT_NAME "opengl32"
    PREFIX ""
)
target_link_options(OpenGLFinal PRIVATE "-static-libgcc" "-static-libstdc++" "-static" "-Wl,-Bstatic,--disable-auto-image-base,--no-seh,--dynamicbase,--nxcompat" "${CMAKE_CURRENT_BINARY_DIR}/opengl32.def")
add_dependencies(OpenGLFinal GenerateDEF)
add_dependencies(GenerateDEF OpenGLIntermediate)

include_directories("./inc")
target_link_libraries(OpenGLFinal PRIVATE DriverClient)