"""
generate_server_plugin.py
=========================

Builds a C++ file that can be compiled to a library object with existing build
systems such as CMake or plain Makefiles.

The resulting shared library can be imported in Python to access the CFFI
`ffi` and `lib` objects, but also linked to from other software which wants
to run Python functions with an embedded interpreter.
"""

import cffi


ffibuilder = cffi.FFI()


# define API that can be used from the Python module
with open("_re_api.h") as f:
    ffibuilder.cdef(f.read())


# add implementations or include headers containing definitions for functions
# defined in _re_api.h
with open("_re_api.cpp") as f:
    ffibuilder.set_source("python_server_plugin", f.read())


# tell CFFI what methods are publicly availabe for the shared library that is
# built his allows it to match those functions and the Python functions
# defined using @ffi.def_extern()
with open("_python_server_plugin.h") as f:
    ffibuilder.embedding_api(f.read())


# make CFFI run some code when the software is loaded
with open("_server_plugin_init.py") as f:
    ffibuilder.embedding_init_code(f.read())


ffibuilder.emit_c_code("_python_server_plugin.cpp")
