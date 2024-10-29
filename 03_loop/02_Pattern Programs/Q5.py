#print this
#   *****
#    ****
#     ***
#      **
#       *
space=0
for st in range(5,0,-1):
    print(space*' ',st*'*',sep='')
    space+=1