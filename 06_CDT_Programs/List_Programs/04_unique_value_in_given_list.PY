# unique value - mean which is available only once in the list
L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
UV=[]
for num in L:
    if L.count(num)==1:
        UV.append(num)
print(UV)



# # Without creating Empty variable
# L = [12, 11, 13, 14, 12, 13, 15, 16, 12]
# for num in L:
#     if L.count(num)==1:
#         print(num)