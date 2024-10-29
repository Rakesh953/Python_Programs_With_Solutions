def Star_Pattern(star,space=3):
    for st in range(1,star+1):
        print(space*' ',st*'*', sep='')
        space-=1
Star_Pattern(4)