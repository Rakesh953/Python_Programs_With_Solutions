import functools
L=[100,22,23,45,55,65]
print(functools.reduce(lambda x,y:x if x>y else y, L))