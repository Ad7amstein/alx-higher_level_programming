#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - frees a listint_t list
 * @p: pointer to list to be freed
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	const char *type_name;
	PyObject *element;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated  = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		element = PyList_GetItem(p, i);
		type_name = Py_TYPE(element)->tp_name;
		printf("Element %ld: %s\n", i, type_name);
	}
}
