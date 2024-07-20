import shelve

T='Hiya'
val=[1,2,3]

# filename='./shelve.out'
# my_shelf = shelve.open(filename,'n') # 'n' for new

# for key in dir():
#     try:
#         my_shelf[key] = globals()[key]
#     except:
#         #
#         # __builtins__, my_shelf, and imported modules can not be shelved.
#         #
#         print('ERROR shelving: {0}'.format(key))
# my_shelf.close()


def save_workspace(filename, names_of_spaces_to_save, dict_of_values_to_save):
    '''
        filename = location to save workspace.
        names_of_spaces_to_save = use dir() from parent to save all variables in previous scope.
            -dir() = return the list of names in the current local scope
        dict_of_values_to_save = use globals() or locals() to save all variables.
            -globals() = Return a dictionary representing the current global symbol table.
            This is always the dictionary of the current module (inside a function or method,
            this is the module where it is defined, not the module from which it is called).
            -locals() = Update and return a dictionary representing the current local symbol table.
            Free variables are returned by locals() when it is called in function blocks, but not in class blocks.

        Example of globals and dir():
            >>> x = 3 #note variable value and name bellow
            >>> globals()
            {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', 'x': 3, '__doc__': None, '__package__': None}
            >>> dir()
            ['__builtins__', '__doc__', '__name__', '__package__', 'x']
    '''
    # print('save_workspace')
    # print('C_hat_bests' in names_of_spaces_to_save)
    # print(dict_of_values_to_save)
    my_shelf = shelve.open(filename,'n') # 'n' for new
    for key in names_of_spaces_to_save:
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

def load_workspace(filename, parent_globals):
    '''
        filename = location to load workspace.
        parent_globals use globals() to load the workspace saved in filename to current scope.
    '''
    my_shelf = shelve.open(filename)
    variables = []
    for key in my_shelf:
        print(key, my_shelf[key])
        variables.append([key, my_shelf[key]])
        a = open(f"vars/{key}", "w")
        a.write(str(my_shelf[key]))
        a.close()

    my_shelf.close()
    print(variables)


# x = 3

# save_workspace('a', dir(), globals())

# load_workspace('a', globals())

def function_call():
    a1 = 12
    c = [""]
    b = {"u": c}
    print(dir()["b"])
    save_workspace('a', dir(), globals())

function_call()
