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
	PyObject *item;
	const char *type_name;

	if (!PyList_Check(p))
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
		item = PyList_GetItem(p, i);
		type_name = Py_TYPE(item)->tp_name;
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
	unsigned char *bytes;
	
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = (unsigned char *)PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", bytes);

	printf("  [.] first %ld bytes:", (size < 10) ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", bytes[i]);
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
	const char *type_name;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	type_name = Py_TYPE(p)->tp_name;

	printf("[.] float object info\n");
	printf("  [.] value: %f\n", value);
	printf("  [.] type: %s\n", type_name);
}
