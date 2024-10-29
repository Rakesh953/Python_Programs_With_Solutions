L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
NewL=[]
hf=0
for num in L:
    if L.count(num)>hf:
        hf=L.count(num)
# print(hf)
    if num not in NewL:
        NewL.append(num)
# print(NewL)
for num in NewL:
    if L.count(num)==hf:
        print(num)

        