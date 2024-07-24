import shelve

print(__name__)
print(__file__)
my_shelf = shelve.open("filename")
variables = []
print(my_shelf)
for key in my_shelf:
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
# print(variables[:][0])
