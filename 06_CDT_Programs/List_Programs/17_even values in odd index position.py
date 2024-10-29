L = [12, 11, 13, 14, 12, 13, 15, 16, 12, 13, 15, 17, 16, 19]
NewL=[]
for ind in range(1,len(L),2):
    print(ind)
    if L[ind]%2==0:
        NewL.append(L[ind])
print(NewL)