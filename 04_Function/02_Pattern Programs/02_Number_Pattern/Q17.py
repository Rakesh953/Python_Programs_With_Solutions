space=4
for sv in range(1,6):
    print(' '*space,end='')
    for num in range(sv,0,-1):
        print(num,end='')
    space-=1
    print()