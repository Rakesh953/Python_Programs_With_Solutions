sp=2
for st in range(1,4,1):
    print(sp*' ',st*'*', sep='')
    sp-=1
sp=1
for st1 in range(2,0,-1):
    print(sp*' ',st1*'*', sep='')
    sp+=1