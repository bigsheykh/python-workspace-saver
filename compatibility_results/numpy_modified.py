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


import numpy as np

save_workspace(3, True, {'np': np})
x = [1.0, 1.0, 1.0, -2.0, np.pi / 2.0, 4.0, 5.0, -10.0, 10.0, 1.0, 2.0, 3.0]
save_workspace(3, False, {'np': np, 'x': x})
save_workspace(4, True, {})
a10 = 10.0
save_workspace(4, False, {'a10': a10})
save_workspace(5, True, {})
an10 = -10.0
save_workspace(5, False, {'an10': an10})
save_workspace(6, True, {})
m1 = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
save_workspace(6, False, {'m1': m1})
save_workspace(8, True, {'min': min, 'np': np, 'm1': m1, 'x': x, 'str': str})
xm_min = str(min(np.ma.core.masked_array(np.array(x), mask=m1)))
save_workspace(8, False, {
    'min': min,
    'np': np,
    'x': x,
    'm1': m1,
    'xm_min': xm_min,
    'str': str
})
save_workspace(10, True, {'np': np, 'm1': m1, 'x': x, 'max': max, 'str': str})
xm_max = str(max(np.ma.core.masked_array(np.array(x), mask=m1)))
save_workspace(10, False, {
    'np': np,
    'str': str,
    'm1': m1,
    'x': x,
    'xm_max': xm_max,
    'max': max
})
save_workspace(12, True, {})
m2 = []
save_workspace(12, False, {'m2': m2})
for x in m1:
    save_workspace(14, True, {'np': np, 'm2': m2, 'x': x})
    m2.append(np.longdouble(x))
    save_workspace(14, False, {'np': np, 'm2': m2, 'x': x})
save_workspace(15, True, {})
m3 = []
save_workspace(15, False, {'m3': m3})
for x in m1:
    save_workspace(17, True, {'np': np, 'm3': m3, 'x': x})
    m3.append(np.longfloat(x))
    save_workspace(17, False, {'np': np, 'm3': m3, 'x': x})
save_workspace(19, True, {'np': np, 'm2': m2})
m4 = np.array(m2).tolist()
save_workspace(19, False, {'np': np, 'm2': m2, 'm4': m4})
save_workspace(20, True, {'np': np, 'm3': m3})
m5 = np.array(m3).tolist()
save_workspace(20, False, {'np': np, 'm3': m3, 'm5': m5})
save_workspace(21, True, {'np': np})
pi_string = np.string_(np.pi)
save_workspace(21, False, {'pi_string': pi_string, 'np': np})
save_workspace(22, True, {'np': np, 'pi_string': pi_string})
pi_unicode = np.unicode_(pi_string)
save_workspace(22, False, {
    'np': np,
    'pi_unicode': pi_unicode,
    'pi_string': pi_string
})
