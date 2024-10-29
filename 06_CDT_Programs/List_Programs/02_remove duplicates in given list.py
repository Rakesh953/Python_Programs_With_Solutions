# L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
# RV=set(L)
# print(RV) # it will show output in set datatype
# print(list(RV)) # it will show output in list datatype


L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
NewL=[]
for n in L:
    if n not in NewL:
        NewL.append(n)
print(NewL)