#include <Python.h>

/**
 * print_python_list_info - frees a listint_t list
 * @p: pointer to list to be freed
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i = 0;
	PyObject *element;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; ++i)
	{
		element = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, element->ob_type->tp_name);
	}
}
