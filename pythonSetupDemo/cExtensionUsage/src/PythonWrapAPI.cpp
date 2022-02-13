#include "foo.h"
#include <string>
#include <python2.7/Python.h>

using namespace std;

/*
Notice：Python Interface Wrap
*/

static PyObject *_myPrint(PyObject *self, PyObject *args)
{
    char *text;

    // 解析 Python 传过来的参数
    if (!PyArg_ParseTuple(args, "s", &text))
        return NULL;

    myPrint(text);
    return Py_None;
}

static PyMethodDef ExtestMethods[] =
{
    { "myPrint", _myPrint, METH_VARARGS },
    { NULL, NULL },
};

PyMODINIT_FUNC initmyprint(void) {
    (void)Py_InitModule("myprint", ExtestMethods);
}