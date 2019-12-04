# basis of a test
    # testing functions or methods, and call ir initialise them
    # having controlled inputs for known outputs
    # testing for these

def make_dough(arg1,arg2):
    if 'water' in [arg1, arg2] and 'flour' in [arg1,arg2]:
        return 'dough'
    else:
        return 'not dough'

def bake_dough(arg3):
    if arg3 == 'dough':
        return 'naan'
    else:
        return 'not naan'

# To make dough: mix water and flour to make dough
print('testing make_dough expect "dough"')
print(make_dough('water','flour') == 'dough')
print('got: ', make_dough('water','flour'))

# when i pass in anything other than flour and water i should get 'not dough'
print('testing make_dough expect "not dough"')
print(make_dough('ice','leaf') == 'not dough')
print('got: ', make_dough('ice','leaf'))

# Baking dough: we should be able to put it in the oven and make naan
print('testing bake_dough expect "naan"')
print(bake_dough('dough') == 'naan')
print('got: ', bake_dough('dough'))

# when i pass in anything other than dough i should get 'not naan'
print('testing bake_dough expect "not naan"')
print(bake_dough('chicken') == 'not naan')
print('got: ', bake_dough('chicken'))