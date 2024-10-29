num=int(input('Enter a number:'))
count=0
for val in range(1,num+1):
    if num%val==0:
        count=count+1
if count==2:
    print(val,'Prime number')
else:
    print(val,'Not a prime number')

    
# # First N numbers
No_P=int(input('Input: '))
num=0
while No_P!=0:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)
        No_P-=1
    num+=1


# Generate between range of number 
S_N=int(input('Starting Number: '))
L_N=int(input('Last Number: '))
for i in range(S_N,L_N+1):
    count=0
    for n in range(1,i+1):
        if i%n==0:
            count+=1
    if count==2:
        print(f'{i} is Prime')
    else:
        print(f'{i} Not')










# c=int(input('Enter the numbers of prime numbers you want: '))
# n=1
# pc=0
# while True:
#     if n>1:
#         for i in range(2,(n//2)+1):
#             if n%i==0:
#                 break
#         else:
#             print(n)
#             pc+=1
#     if c==pc:
#         break
#     n+=1




# Without counting the divisior    
# n=int(input('enter a a number:'))
# if n<=1:
#   print('Not prime')
# else:
#   for i in range(2,(n//2)+1):
#     if n%i==0:
#       print('Not prime')
#       break
#   else:
#     print('Prime')