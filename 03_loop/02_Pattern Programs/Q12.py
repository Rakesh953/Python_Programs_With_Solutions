for st0 in range(1,5):
    for st1 in range(1,9):
        if st1<=st0 or st1>=9-st0:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
for st0 in range(3,0,-1):
    for st1 in range(1,9):
        if st1<=st0 or st1>=9-st0:
            print('*',end='')
        else:
            print(' ',end='')
    print()