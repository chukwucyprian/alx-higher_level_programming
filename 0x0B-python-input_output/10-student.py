#!/usr/bin/python3
""" A class that gives more student data """


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the Student instance.

        """
        if attrs is None:
            # If attrs is not provided, retrieve all attributes
            attrs = self.__dict__.keys()
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
