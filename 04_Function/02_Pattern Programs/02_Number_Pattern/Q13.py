space=0
for ev in range(0,5):
    print(' '*space, end='')
    for num in range(5,ev,-1):
        print(num,end='')
    space+=1
    print()