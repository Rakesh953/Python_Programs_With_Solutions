def Star_Pattern(star,space=0):
    for st in range(star,0,-1):
        print(space*' ',st*'*', sep='')
        space+=1
Star_Pattern(4)