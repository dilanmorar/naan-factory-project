# basis of a test
    # testing functions or methods, and call ir initialise them
    # having controlled inputs for known outputs
    # testing for these

def make_dough(arg1,arg2):
    pass

def bake_dough(arg3):
    pass

# To make dough: mix water and flour to make dough
print('testing make_dough expect "dough"')
print(make_dough('water','flour') == 'dough')
print('got: ', make_dough('water','flour'))

# Baking dough: we should be able to put it in the oven and make naan
print('testing bake_dough expect "naan"')
print(bake_dough('dough') == 'naan')
print('got: ', bake_dough('dough'))