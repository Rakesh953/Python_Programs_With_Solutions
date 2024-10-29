# L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
# for n in L:
#     print(L[1::2])

L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
for n in range(len(L)):
    if n%2!=0:
        print(L[n])

# print value numbers in even index position?
L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
for n in range(len(L)):
    if n%2==0:
        print(L[n])