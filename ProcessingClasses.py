# ---------------------------------------------------------- #
# Title: Processing Classes
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JHenderson,9.6.2022,Modified module to complete Assignment09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to be run by itself")


class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JHenderson,9.6.2022,Modified Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Writes data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of method's successful completion
        """
        success_status = False
        try:  # try to open file and write list of objects to it, then save and close
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")  # add a new line after writing each object to the file
            file.close()
            success_status = True  # set success status to True if no errors were encountered
        except Exception as e:  # raise exception if writing error occurred, print details
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads comma-delimited data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:  # try to open file and read list of objects from it, then close when done
            file = open(file_name, "r")
            for line in file:
                row = line.strip().split(",")  # strip and split apart data delimited by commas in the file
                list_of_rows.append(row) # add data to list of object rows
            file.close()
        except Exception as e:  # raise exception if reading error occurred, print details
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

# class DatabaseProcessor:
#     pass
#     # TODO: Add code to process to and from a database
