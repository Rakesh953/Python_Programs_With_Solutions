# L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
# print(max(L))

#    or 
L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
HV=L[0]
for num in L:
    if num>HV:
        HV=num
print(HV)

