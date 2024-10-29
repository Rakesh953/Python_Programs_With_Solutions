S = 'ENGINEERING'
NewS=''
for ch in S:
    if ch not in NewS:
        NewS+=ch
for ch in NewS:
    if S.count(ch)>1:
        print(ch)

# S='RAKESH MEHER'
rev=''
DC=''
for i in S:
    if i in rev and i not in DC:
        DC+=i
    else:
        rev+=i
print(DC)