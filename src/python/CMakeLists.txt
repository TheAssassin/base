cmake_minimum_required(VERSION 2.8.11)

project(python_plugins)

set(plugin_deps python3 sdl2)

# configure dependencies with pkg-config
foreach(dep IN LISTS plugin_deps)
    pkg_check_modules(${dep} REQUIRED ${dep})

    # add the necessary includes
    foreach(include_dir IN LISTS ${dep}_INCLUDE_DIRS)
        include_directories(${include_dir})
    endforeach(include_dir)

    # link to the libraries
    foreach(lib IN LISTS ${dep}_LIBRARIES)
        link_libraries(${lib})
    endforeach(lib)

    # tell the compiler where to find the libraries' binaries
    foreach(lib_dir IN LISTS ${dep}_LIBRARY_DIRS)
        link_directories(${lib_dir})
    endforeach(lib_dir)
endforeach(dep)

include_directories(
    ${PROJECT_SOURCE_DIR}
    ${PROJECT_SOURCE_DIR}/../enet/include
)

add_custom_command(
    OUTPUT ${PROJECT_SOURCE_DIR}/_python_server_plugin.cpp
    COMMAND python3 generate_server_plugin.py
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    DEPENDS
    ${PROJECT_SOURCE_DIR}/generate_server_plugin.py
    ${PROJECT_SOURCE_DIR}/_re_api.cpp
    ${PROJECT_SOURCE_DIR}/_re_api.h
)

add_library(
    python_server_plugin
    SHARED
    ${PROJECT_SOURCE_DIR}/_python_server_plugin.cpp
)
