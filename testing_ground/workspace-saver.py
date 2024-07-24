import shelve
import os
import base64

def save_workspace(line_number, is_before_line, dict_of_values_to_save):
    os.makedirs("/tmp/python-workspace/", exist_ok=True)
    dir_name = base64.b64encode(__file__.encode()).decode()
    os.makedirs(f"/tmp/python-workspace/{dir_name}", exist_ok=True)
    my_shelf = shelve.open(
        f'/tmp/python-workspace/{dir_name}/{line_number}/{is_before_line}.db', 'n')
    for key in globals().keys():
        try:
            my_shelf[key] = globals()[key]
        except TypeError:
            #
            # __builtins__, my_shelf, and imported modules can not be shelved.
            #
            print(f'TypeError shelving: {key}')
        except:
            print(f'Error shelving: {key}')

    for key in dict_of_values_to_save.keys():
        try:
            my_shelf[key] = dict_of_values_to_save[key]
        except TypeError:
            #
            # __builtins__, my_shelf, and imported modules can not be shelved.
            #
            print(f'TypeError shelving: {key}')
        except:
            print(f'Error shelving: {key}')

    my_shelf.close()
