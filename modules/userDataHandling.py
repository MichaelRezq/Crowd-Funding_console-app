# Python program to update
# JSON


import json

import os
print(os.getcwd())
# function to add to JSON


def append_json(new_data, filename):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file)
        file.close()


def read_jaon(filename):
    with open(filename, 'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        file.close()
        return file_data


# Data to be written
def write_json(new_data, filename):

    with open(filename, "w") as filename:
        json.dump(new_data, filename)
