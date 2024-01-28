#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <wchar.h>
#include <unicodeobject.h>

/**
 * print_python_string - This function prints information about python
 * @p: The first parameter
 */
void print_python_string(PyObject *p)
{
	long int l;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	l = ((PyASCIObject *)(p))->l;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", l);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &l));
}
