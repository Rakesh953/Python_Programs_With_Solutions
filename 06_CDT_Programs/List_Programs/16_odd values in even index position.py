L=[3,8,2,3,4,5,6,7,8,7,7,9]
NewL = []
for ind in range(0, len(L), 2): 
    if L[ind] % 2 != 0: 
        # print(L[ind]) # this will print without list format
        NewL.append(L[ind])
print(NewL)


# for i in range(len(L)):
#     if i%2==0:
#         if L[i]%2!=0:
#             print(L[i])



# NewL=[]
# for i in range(len(L)):
#     if i%2==0:
#         if L[i]%2!=0:
#             NewL.append(L[i])
# print(NewL)