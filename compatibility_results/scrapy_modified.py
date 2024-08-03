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


import scrapy
from warnings import catch_warnings

save_workspace(5, True, {})
d = {'a': 123, u'b': b'c', u'd': u'e', 77: u'e'}
save_workspace(5, False, {'d': d})
save_workspace(6, True, {'scrapy': scrapy, 'd': d})
d2 = scrapy.utils.python.stringify_dict(d, keys_only=False)
save_workspace(6, False, {'d2': d2, 'd': d, 'scrapy': scrapy})
save_workspace(8, True, {})
tuples = [('a', 123), (u'b', 'c'), (u'd', u'e'), (77, u'e')]
save_workspace(8, False, {'tuples': tuples})
save_workspace(9, True, {'tuples': tuples, 'dict': dict})
d3 = dict(tuples)
save_workspace(9, False, {'d3': d3, 'tuples': tuples, 'dict': dict})
save_workspace(10, True, {'scrapy': scrapy, 'tuples': tuples})
d4 = scrapy.utils.python.stringify_dict(tuples, keys_only=False)
save_workspace(10, False, {'scrapy': scrapy, 'tuples': tuples, 'd4': d4})
save_workspace(12, True, {})
d5 = {'a': 123, u'b': 'c', u'd': u'e', 77: u'e'}
save_workspace(12, False, {'d5': d5})
save_workspace(13, True, {'scrapy': scrapy, 'd5': d5})
d6 = scrapy.utils.python.stringify_dict(d5)
save_workspace(13, False, {'scrapy': scrapy, 'd6': d6, 'd5': d5})
with catch_warnings(record=True) as warnings:
    save_workspace(16, True, {'scrapy': scrapy})
    a_dict_item = scrapy.item.DictItem()
    save_workspace(16, False, {'scrapy': scrapy, 'a_dict_item': a_dict_item})
    save_workspace(17, True, {
        'len': len,
        'warnings': warnings,
        'print': print
    })
    print(len(warnings))
    save_workspace(17, False, {
        'len': len,
        'warnings': warnings,
        'print': print
    })
