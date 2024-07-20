import shelve
filename='a'


# Open the file
my_shelf = shelve.open(filename)

# loop on my_shelf
for key in my_shelf:
    # Set globals
    
    # Print the key
    print(key)
    try:
        globals()[key]=my_shelf[key]
    except TypeError:
        #
        # __builtins__, my_shelf, and imported modules can not be shelved.
        #
        print(f'TypeError shelving: {key}')
    except:
        print(f'Error shelving: {key}')

# Close it
my_shelf.close()
