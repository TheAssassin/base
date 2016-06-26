/*
 * Definition of C function signatures that can be called using the CFFI module.
 *
 * This header file will only be used by CFFI, which means it cannot contain any preprocessor directives such as
 * #include. These directives have to be put into _re_api.cpp.
 *
 * This file can contain both the signatures of (wrapper) functions that are defined in _re_api.cpp and the signatures
 * of functions of external libraries whose headers have been included in _re_api.cpp. The signatures can either be
 * copied from these headers or in some cases from the libraries' man pages.
 */

void reConoutf(char message[]);

int reGetServerPort();

void reShutdownServer();
