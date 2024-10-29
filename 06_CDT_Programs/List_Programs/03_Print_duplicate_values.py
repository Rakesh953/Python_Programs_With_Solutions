L=[1, 2, 3, 1, 3]
NewL=[]
D_value=[]
for i in L:
    if i in NewL and i not in D_value:
        D_value.append(i)
    else:
        NewL.append(i)
print(D_value)





L = [1, 2, 3, 1, 3]
NewL = []
# Find all unique elements
for n in L:
    if n not in NewL:
        NewL.append(n)
# Print only the duplicate values
for n in NewL:
    if L.count(n) > 1:
        print(n)



        # OR 
        


l=[1, 2, 3, 1, 3]
l1=[]
for i in l:
  if l.count(i) > 1 and i not in l1:
    l1.append(i)
print(l1)
