space=0
for ev in range(5,0,-1):
    print(' '*space,end='')
    for num in range(1,ev+1):
        print(num,end='')
    space+=1
    print()