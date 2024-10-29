def Star_Pattern(star,space=0):
    for st in range(star, 0, -2):
        print(' '*space, '*'*st, sep='')
        space+=1
Star_Pattern(7)
def Star_Pattern2(star,space=2):
    for st in range(3,star+1,2):
        print(' '*space, '*'*st, sep='')
        space-=1
Star_Pattern2(7)