space=0
for sv in range(5,0,-1):
    print(' '*space, end='')
    for num in range(sv,0,-1):
        print(num,end='')
    space+=1
    print()