#include <Python.h>
/**
 * print_python_list_info - nbvhjb
 * @p: fcxdsza
 * Return: njhb
 */
void print_python_list_info(PyObject *p)
{
	int se, oc, z;
	PyObject *suv;

	se = Py_SIZE(p);
	oc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", se);
	printf("[*] Allocated = %d\n", oc);

	for (z = 0; z < se; z++)
	{
		printf("Element %d: ", z);

		suv = PyList_GetItem(p, z);
		printf("%s\n", Py_TYPE(suv)->tp_name);
	}
}
