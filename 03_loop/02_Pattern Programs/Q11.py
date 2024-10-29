# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******
sp=0
for st in range(7,0,-2):
    print(sp*' ',st*'*', sep='')
    sp+=1
sp=2
for st in range(3,8,2):
    print(sp*' ',st*'*', sep='')
    sp-=1