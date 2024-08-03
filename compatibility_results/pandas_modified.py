import shelve
import os
import base64


def save_workspace(line_number, is_before_line, dict_of_values_to_save):
    os.makedirs('/tmp/python-workspace/', exist_ok=True)
    dir_name = base64.b64encode(os.path.abspath(__file__).encode()).decode()
    py_directory = '/tmp/python-workspace/' + dir_name
    os.makedirs(py_directory, exist_ok=True)
    line_directory = py_directory + '/' + str(line_number)
    os.makedirs(line_directory, exist_ok=True)
    file_name = line_directory + '/' + str(is_before_line)
    my_shelf = shelve.open(file_name, 'n')
    for key in globals().keys():
        try:
            my_shelf[key] = globals()[key]
        except TypeError:
            print('TypeError shelving:', key)
        except:
            print('Error shelving:', key)
    for key in dict_of_values_to_save.keys():
        try:
            my_shelf[key] = dict_of_values_to_save[key]
        except TypeError:
            print('TypeError shelving:', key)
        except:
            print('TypeError shelving:', key)
    my_shelf.close()


import pandas

save_workspace(4, True, {})
array = [[1, 2, 3], [4, 'hello', 6], [7, 8, 9]]
save_workspace(4, False, {'array': array})
save_workspace(7, True, {'array': array, 'list': list, 'pandas': pandas})
df_a = list(pandas.DataFrame(array, columns=['A', 2, 'C'])['A'] + 1)
save_workspace(7, False, {
    'array': array,
    'list': list,
    'pandas': pandas,
    'df_a': df_a
})
save_workspace(8, True, {'array': array, 'list': list, 'pandas': pandas})
df_2 = list(pandas.DataFrame(array, columns=['A', 2, 'C'])[2] * 2)
save_workspace(8, False, {
    'array': array,
    'pandas': pandas,
    'list': list,
    'df_2': df_2
})
save_workspace(9, True, {'array': array, 'list': list, 'pandas': pandas})
df_c = list(pandas.DataFrame(array, columns=['A', 2, 'C'])['C']**2)
save_workspace(9, False, {
    'array': array,
    'pandas': pandas,
    'df_c': df_c,
    'list': list
})
save_workspace(11, True, {'array': array, 'pandas': pandas})
pandas.DataFrame.from_dict(
    pandas.DataFrame(array, columns=['A', 2,
                                     'C']).to_dict()).info(null_counts=True)
save_workspace(11, False, {'array': array, 'pandas': pandas})
