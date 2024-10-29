sp=4
count=1
for num in range(5,0,-1):
    print(sp*' ',str(num)*count, sep='')
    sp-=1
    count+=1