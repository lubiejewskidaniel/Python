# exporter.py file for OOP - class Exporter to accomplish last assessment point

import csv  # Importing csv module, to allow to read from and write to CSV (Comma-Separated Values) files
import json  # Importing the json module, which is a standard Python module for encoding and decoding JSON
# (JavaScript Object Notation) data


class Exporter:  # Defining a new class named "Exporter"
    # Below as you can see I created 3 staticmethod using "@staticmethod", static method is a method that belongs
    # to a class instead of instance of the class.

    @staticmethod
    def export_to_txt(exporter, filename):
        with open(filename, 'w') as file:
            file.write(str(exporter.get_aggregate_info()))

    @staticmethod
    def export_to_csv(exporter, filename):  # Defining a method named "export_to_txt" within the "Exporter" class.
        # This method takes three parameters: "self" , "park", and "filename".
        with open(filename, 'w', newline='') as file:  # Opening a file specified by "filename" in write mode,
            # and it's using the "with" statement to be sure of the proper handling of the file (automatic closing)
            # even if an exception occurs within the indented block.
            # "newline=''" argument is used to handle line endings in a way suitable for CSV file writing.
            writer = csv.writer(file)  # Creating a CSV writer, kind of object linked with the opened file.
            writer.writerow(['Number of reviews',
                             'Number of positive reviews',
                             'Average review score',
                             'Number of countries reviewed'])
            # Code above writing a header row to the CSV file, actually column names.
            writer.writerow(list(exporter.get_aggregate_info().values()))  # Writing a data row to the CSV file,
            # converting the values of the aggregate information from the park object into a list.

    @staticmethod
    def export_to_json(exporter, filename):  # Defining a third method, "export_to_json", within the "Exporter"
        # class, with parameters similar to the previous methods.
        with open(filename, 'w') as file:  # Similar to the previous methods, this line opening a file
            # specified by the "filename" in write mode "w" using a "with" statement.
            json.dump(exporter.get_aggregate_info(), file, indent=2)  # Using  json dump() method to write
            # the aggregate information from the "park" object to the opened "file" in JSON format with an
            # indentation of 2 spaces "indent=2".
