# num=int(input('Enter the number: '))
# Factor_sum=0
# for val in range(1,(num//2)+1):
#     if num%val==0:
#         Factor_sum=Factor_sum+val
#         print(val) #to see tho far its going to run (it will check halp of the input numner)
# if num==Factor_sum:
#     print('Perfect Number')
# else:
#     print('Not a perfect number')



# or 
# num = 6
# Fsum=0
# for val in range(1,num+1):
#     if num%val==0:
#         Fsum+=val
# if num*2==Fsum:
#     print('Perfect')
# else:
#     print('Not Perfect')


# First N numbers
No_P=int(input('Input: '))
num=1
while No_P!=0:
    sum=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            sum+=i
    if num==sum:
        print(num)
        No_P-=1
    num+=1