# ---------------------------------------------------------- #
# Title: Data Classes
# Description: A module of data classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JHenderson,9.6.2022,Modified module to complete Assignment09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to be run by itself")

class Person:
    """Stores data about a person:

    properties:
        first_name: (string) with the person's first name

        last_name: (string) with the person's last name
    methods:
        to_string() returns comma-separated data about a Person (alias for __str__())
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JHenderson,9.6.2022,Modified Class
    """

    # -- Constructor --
    def __init__(self, first_name: str, last_name: str):
        # -- Attributes --
        self.first_name = first_name  # Person is initiated with a first and last name
        self.last_name = last_name

    # -- Properties --
    @property
    def first_name(self):  # return first name in title case
        return str(self.__first_name).title()

    @first_name.setter
    def first_name(self, value: str):  # sets person's first name
        if str(value).isalpha():  # raise exception if name doesn't contain all letters
            self.__first_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def last_name(self):  # return last name in title case
        return str(self.__last_name).title()

    @last_name.setter
    def last_name(self, value: str):  # sets person's last name
        if str(value).isalpha():  # raise exception if name doesn't contain all letters
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns a string with this object's data """
        return self.first_name + ',' + self.last_name  # concatenates first & last name with a comma separator


class Employee(Person):  # Inherits from Person
    """Stores data about an employee:

    properties:
        employee_id: (int) with the employee's ID

        first_name: (string) with the employee's first name

        last_name: (string) with the employee's last name
    methods:
        to_string() returns comma-separated employee data (alias for __str__())
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JHenderson,9.7.2022,Modified Class
    """

    def __init__(self, employee_id: int, first_name: str, last_name: str):
        # Attributes
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    # --Properties--
    @property
    def employee_id(self):  # returns an employee's ID number
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value: int):  # sets an employee's ID
        if str(value).isnumeric():  # raise an exception if the ID contains characters that aren't numbers
            self.__employee_id = value
        else:
            raise Exception("IDs must be numbers")

    # --Methods--
    def to_string(self):  # Overrides the original method (polymorphic)
        """ Explicitly returns a string with this object's data """
        # Linking to self.__str__() does not work with inheritance
        data = super().__str__()  # get data from parent (super) class
        return str(self.employee_id) + ',' + data  # returns employee ID, first and last name

    def __str__(self):  # Overrides the original method (polymorphic)
        """ Implicitly returns field data """
        data = super().__str__()  # get data from parent(super) class
        return str(self.employee_id) + ',' + data  # returns employee ID, first and last name
    # --End of Class --
