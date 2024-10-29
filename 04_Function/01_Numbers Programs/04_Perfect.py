def Perfect(num,sum=0):
    for n in range(1,(num//2)+1):
        if num%n==0:
            sum+=n
    return sum==num
num=int(input('Enter the number: '))
print(Perfect(num))


# First N numbers
def N_Perfect(No_P, num=1):
    while No_P != 0:
        sum = 0
        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                sum += i
        if num == sum:
            print(num) 
            No_P -= 1
        num += 1
No_P = int(input('Input: '))
N_Perfect(No_P)


# # Generate between range of number
# def Perfect(First,Last):
#     for i in range(First,Last+1):
#         sum=0
#         for num in range(1,(i//2)+1):
#             if i%num==0:
#                 sum+=num
#         if i==sum:
#             print(f'{i} Perfect')
#         else:
#             print(f'{i} Not')
# First=int(input('Enter the first number: '))
# Last=int(input('Enter the second number: '))
# Perfect(First, Last)