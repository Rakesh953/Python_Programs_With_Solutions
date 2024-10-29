# To calculate sum of all element 
import functools
L=[100,22,23,45,55]
print(functools.reduce(lambda x,y:x+y,L))