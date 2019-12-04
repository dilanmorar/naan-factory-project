# here we run the functions

from naan_factory_functions import *

print('Can you make naan?')
ing1 = input('What is you first ingredient? ').lower()
ing2 = input('What is your second ingredient? ').lower()

output1 = make_dough(ing1,ing2)
output2 = bake_dough(output1)

print('Baked ' + ing1 + ' mixed with '+ ing2 + ', this is ' + output2)