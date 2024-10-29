L1=[2,1,3,4,5]
L2=[7,1,6,4,7]
sum=[]
for i in range(len(L1)):
   #  print(i) i is used for finding same index position  
    sum.append(L1[i] + L2[i])
print(sum)