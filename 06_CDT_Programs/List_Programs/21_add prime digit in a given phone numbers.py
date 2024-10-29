# PH = [9078895125]
# sum = 0
# for ind in str(PH[0]):  # Convert the number to a string and iterate
#     rem = int(ind)  # Convert each character back to an integer
#     count = 0
#     for num in range(1, rem + 1):
#         if rem % num == 0:
#             count += 1
#     if count == 2: 
#         sum += rem
# print(sum)

PH=[9,0,7,8,8,9,5,1,2,5]
sum=0
for ind in PH:
    count=0
    for n in range(1,ind+1):
        if ind%n==0:
            count+=1
    if count==2:
        sum+=ind
print(sum)