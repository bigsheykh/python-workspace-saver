import shelve

before_shelf = shelve.open(str(True))
after_shelf = shelve.open(str(False))

for key in before_shelf:
    try:
        globals()[key] = before_shelf[key]
    # except TypeError:
        #
        # __builtins__, my_shelf, and imported modules can not be shelved.
        #
        # print('TypeError shelving:', key)
    except:
        pass
        # print('Error shelving:', key)
