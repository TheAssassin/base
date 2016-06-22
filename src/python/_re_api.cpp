/*
 * Implementation of functions defined in _re_api.h.
 *
 * Since re_api.h can contain signatures of external functions, too, it is possible to include external headers here
 * and define signatures of specific functions in _re_api.h.
 */

#include "cube.h"

void pysrvConoutf(char message[]) {
    conoutf("%s", message);
}
