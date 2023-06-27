#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the Python object
 *
 * Return: None
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	if (!p || !PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type_name = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);
	}
}

/** 
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the Python object
 *
 * Return: None
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	Py_ssize_t max_print = 10;

	if (!p || !PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	size = PyBytes_Size(p);
	PyObject *repr = PyObject_Repr(p);
	const char *repr_str = PyUnicode_AsUTF8(repr);

	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", repr_str);
	printf("  [.] first %ld bytes:", size < max_print ? size : max_print);

	for (i = 0; i < size && i < max_print; i++)
	{
		printf(" %02x", PyBytes_AS_STRING(p)[i] & 0xff);
	}

	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to the Python object
 *
 * Return: None
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!p || !PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  [.] value: %f\n", value);
	printf("  [.] type: %s\n", Py_TYPE(p)->tp_name);
}
