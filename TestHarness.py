# ---------------------------------------------------------- #
# Title: Test Harness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JHenderson,9.6.2022,Modified script to test Person, Employee, FileProcessor and EmployeeIO classes
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    from IOClasses import EmployeeIO as Eio  # employee io class
else:
    raise Exception("This file was not created to be imported")

# Test data module - Person
objP1 = D.Person("Bob", "Smith")

# try:
#     objP1 = D.Person("Bob123", "Smith")
#     objP1.first_name = "Bob234"
# except Exception as e:
#     print(e, e.__doc__, type(e), sep='\n')
#     pass

objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module - Person
P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    p = D.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))

# Test data module - Employee
employee_1 = D.Employee(1, "Noelle", "Nguyen")
employee_2 = D.Employee(2, "Raj", "Tillimook")
employees = [employee_1, employee_2]
for e in employees:
    print(e.to_string(), type(e))

# Test processing module - Employee
P.FileProcessor.save_data_to_file("EmployeeData.txt", employees)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    e = D.Employee(row[0], row[1], row[2])
    print(e.to_string().strip(), type(e))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
Eio.print_current_list_items(employees)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
