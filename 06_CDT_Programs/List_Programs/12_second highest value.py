# L=[6,7,2,3,4,5,6,7,8]
# unique_L = list(set(L))  # Remove duplicates by converting to a set and back to a list
# unique_L.sort()  # Sort the list in ascending order
# SH = unique_L[-2]  # The second last element will be the second highest

# print(SH)

# L = [6,7,2,3,4,5,6,7,8]
# NewL = []
# # Step 1: Create a new list with unique elements
# for num in L:
#     if num not in NewL:
#         NewL.append(num)
# # Step 2: Find the highest value in the unique list
# HV = NewL[0]
# for num in NewL[1:]:
#     if num > HV:
#         HV = num
# # Step 3: Remove the highest value
# NewL.remove(HV)
# # Step 4: Find the second highest value
# HV = NewL[0]
# for num in NewL[1:]:
#     if num > HV:
#         HV = num
# # Print the second highest value
# print(HV)



# L = [6,7,2,3,4,5,6,7,8]
# HV = L[0]
# SH = None
# for num in L:
#     if num > HV:
#         SH = HV
#         HV = num
#     elif SH is None or (num > SH and num < HV):
#         SH = num
# print(SH)


L=[6,7,2,3,4,5,6,7,8]
NewL=[]
for i in L:
    if i not in NewL:
        NewL.append(i)
NewL.sort()
print(NewL[-2])