import shelve
import os
import base64

def save_workspace(line_number, is_before_line, dict_of_values_to_save):
    os.makedirs("/tmp/python-workspace/", exist_ok=True)
    dir_name = base64.b64encode(os.path.abspath(__file__).encode()).decode()
    py_directory = "/tmp/python-workspace/" + dir_name
    os.makedirs(py_directory, exist_ok=True)
    line_directory = py_directory + "/" + str(line_number)
    os.makedirs(line_directory, exist_ok=True)
    file_name = line_directory + "/" + str(is_before_line)
    my_shelf = shelve.open(file_name, 'n')
    for key in globals().keys():
        try:
            my_shelf[key] = globals()[key]
        except TypeError:
            #
            # __builtins__, my_shelf, and imported modules can not be shelved.
            #
            print('TypeError shelving:', key)
        except:
            print('Error shelving:', key)

    for key in dict_of_values_to_save.keys():
        try:
            my_shelf[key] = dict_of_values_to_save[key]
        except TypeError:
            #
            # __builtins__, my_shelf, and imported modules can not be shelved.
            #
            print('TypeError shelving:', key)
        except:
            print('TypeError shelving:', key)

    my_shelf.close()
