sp=4
for ev in range(1,6):
    print(' '*sp, end='')
    for num in range(1,ev+1):
        print(num, end='')
    sp-=1
    print()