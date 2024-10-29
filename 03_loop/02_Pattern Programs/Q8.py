#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
sp=3
for st in range(1,6,2):
    print(sp*' ',st*'*',sep='')
    sp-=1
sp=0
for st1 in range(7,0,-2):
    print(sp*' ',st1*'*', sep='')
    sp+=1