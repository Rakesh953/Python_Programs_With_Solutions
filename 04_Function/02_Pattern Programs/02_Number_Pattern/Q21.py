space=0
count=5
for num in range(1,6):
    print(' '*space, str(num)*count, sep='')
    space+=1
    count-=1