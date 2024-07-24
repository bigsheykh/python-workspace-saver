import shelve
from threading import active_count
from multiprocessing.pool import AsyncResult

class A:
    def __init__(self) -> None:
        self.a = ""

    def b(self):
        print(type(self))
        print(type(self.b))
        print(self.b.__module__)
        dict_of_values_to_save.update({"self": self})


def x(self):
    self.b()

my_shelf = shelve.open("filename")
variables = []
print(my_shelf)
for key in my_shelf:
    print(key)
    # print(key, my_shelf[key])
    # variables.append([key, my_shelf[key]])
    # a = open(f"vars/{key}", "w")
    # a.write(str(my_shelf[key]))
    # a.close()
    try:
        # print(key, my_shelf[key])
        variables.append([key, my_shelf[key]])
        globals()[key] = my_shelf[key]
    except TypeError:
        #
        # __builtins__, my_shelf, and imported modules can not be shelved.
        #
        print(f'TypeError shelving: {key}')
    except:
        print(f'Error shelving: {key}')

# print(my_shelf["x"])
my_shelf.close()

print(self)
exit()



dict_of_values_to_save = {}

b = A()
b.b() 

self = b

print(self.__module__)       
self.b()
x(self)
m11 = 11
print(active_count.__module__)
print(AsyncResult.__module__)

dict_of_values_to_save.update({"A": A, "b": b, "m11": m11,
                          "x":x, "active_count": active_count, "AsyncResult": AsyncResult,
                          "print": print})

my_shelf = shelve.open("filename",'n') # 'n' for new
if True:
    xx = 11
    dict_of_values_to_save.update({"xx": xx})

print(dict_of_values_to_save)
for key in dict_of_values_to_save.keys():
    # try:
    # print(key, type(dict_of_values_to_save[key]), dict_of_values_to_save[key].__module__)
    # print(key, type(dict_of_values_to_save[key].__module__))
    my_shelf[key] = dict_of_values_to_save[key]
    # except TypeError:
    #     #
    #     # __builtins__, my_shelf, and imported modules can not be shelved.
    #     #
    #     print(f'TypeError shelving: {key}')
    # except:
    #     print(f'Error shelving: {key}')

my_shelf["dict_of_values_to_save"] = dict_of_values_to_save

# for key in dir():
#     try:
#         my_shelf[key] = globals()[key]
#     except TypeError:
#         #
#         # __builtins__, my_shelf, and imported modules can not be shelved.
#         #
#         print(f'TypeError shelving: {key}')
#     except:
#         print(f'Error shelving: {key}')

my_shelf.close()

