# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# James Henderson,09.07.2022,Added code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    from IOClasses import EmployeeIO as Eio  # employee io class
else:
    raise Exception("This file was not created to be imported")

# Data - Start  ---------------------------------------------------- #
EMPLOYEE_DATA_FILE = 'EmployeeData.txt'  # file containing Employee data
employees = []  # list of Employee objects
# Data - End  ---------------------------------------------------- #


# Custom Error Classes - Start  -------------------------------------------- #
class InvalidUserMenuChoice(Exception):
    """ Custom error class for when user enters an invalid menu choice.

    changelog: (When,Who,What)
        James Henderson,08.30.2022,Created class code
    """
    pass
# Custom Error Classes - End  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
data = P.FileProcessor.read_data_from_file(EMPLOYEE_DATA_FILE)
for row in data:
    emp = D.Employee(row[0], row[1], row[2])
    employees.append(emp)

# Show user a menu of options
while True:
    Eio.print_menu_items()  # Shows main menu

    try:
        choice_str = Eio.input_menu_options()  # Get user menu selection
        if choice_str.strip() == '1':  # Show user current data in the list of employee objects
            Eio.print_current_list_items(employees)
        elif choice_str.strip() == '2':  # Let user add data to the list of employee objects
            new_emp = Eio.input_employee_data()
            employees.append(new_emp)
            Eio.print_current_list_items(employees)
        elif choice_str.strip() == '3':  # let user save current data to file
            status = P.FileProcessor.save_data_to_file(EMPLOYEE_DATA_FILE, employees)
            if status:  # print a message to the user based on the save status
                print("Employee data saved.")
            else:
                print("Save failed.")
        elif choice_str.strip() == '4':  # Let user exit program
            print("Goodbye!")
            break  # and exit

        else:  # go to error handling - prompt the user for a valid menu choice if an invalid choice was entered
            raise InvalidUserMenuChoice("Invalid menu choice.")

    except InvalidUserMenuChoice:  # if invalid choice, let the user know; repeat prompt
        print("Please enter a valid choice [1-5].")

# Main Body of Script  ---------------------------------------------------- #

