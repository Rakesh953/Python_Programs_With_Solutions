space=4
for sv in range(5,0,-1):
    print(' '*space,end='')
    for num in range(sv,6):
        print(num,end='')
    space-=1
    print()