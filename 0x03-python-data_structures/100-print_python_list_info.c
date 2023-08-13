#include "Python.h"
/**
 * print_python_list_info - frees a listint_t list
 * @p: pointer to list to be freed
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p), i;
	const char *type_name;
	PyObject *element;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated  = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		element = PyList_GET_ITEM(p, i);
		type_name = element->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);
	}
}
