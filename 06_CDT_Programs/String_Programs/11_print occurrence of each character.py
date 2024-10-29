# Input-
# S = 'Engineering'
# Output-
# 'E' occurs 1 times
# 'n' occurs 3 times
# 'g' occurs 2 times
# 'i' occurs 2 times
# 'e' occurs 3 times
# 'r' occurs 1 times

S='ENGINEERING'
NewS=''
for ch in S:
    if ch not in NewS:
        NewS+=ch
for c in NewS:
    print(f'{c} = {S.count(c)}')

