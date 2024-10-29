def Star_Pattern(star,space=2):
    for st in range(1,star+1):
        print(' '*space, '*'*st, sep='')
        space-=1
Star_Pattern(3)
def Star_Pattern2(star,space=1):
    for st in range(star,0,-1):
        print(' '*space, '*'*st, sep='')
        space+=1
Star_Pattern2(2)