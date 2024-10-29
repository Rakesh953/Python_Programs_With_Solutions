# L = [12, 11, 13, 14, 12, 13, 15, 16, 12, 13, 15, 17, 16, 19]
# sum=0
# for num in L:
#     if num>1:
#         count=0
#         for val in range(1,num+1):
#             if num%val==0:
#                 count+=1
#         if count==2:
#             sum+=num
# print(sum)



L=[1,3,2,3,4,5,6,1,7,8,9,10,11]
sum=0
for num in L:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        sum+=num
print(sum)

