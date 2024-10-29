#     A
#    BB
#   CCC
#  DDDD
# EEEEE

S='ABCDE'
space=4
count=1
for st in S:
    print(' '*space, st*count,sep='')
    space-=1
    count+=1

# Using Slicing
S = 'ABCDE'
space = 4
for i in range(1, len(S) + 1):
    print(' ' * space, S[i-1] * i, sep='')
    space -= 1
