S='ENGINEERING'
hf=0
NewS=''
for ch in S:
    if S.count(ch)>hf:
        hf=S.count(ch)
    if ch not in NewS:
        NewS+=ch
# print(NewS)
for ch in NewS:
    if S.count(ch)==hf:
        print(ch)