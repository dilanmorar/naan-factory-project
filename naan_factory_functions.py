# functions go here

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

def run_factory(arg1,arg2):
    output1 = make_dough()
    output2 = bake_dough(output1)
    return output2