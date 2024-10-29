def Niven(num,c_num,sum=0):
    while num!=0:
        rem=num%10
        sum+=rem
        num//=10
    return c_num%sum==0

        # or
         
    # if c_num%sum==0:
    #     return True
    # return False

num=int(input('Enter the number: '))
print(Niven(num,c_num=num))



# First N numbers
def N_Niven(No_Nvn, num=1):
    while No_Nvn != 0:
        c_num = num 
        sum = 0      
        while c_num!=0:
            rem = c_num % 10 
            sum += rem        
            c_num //= 10      
        if num % sum == 0:
            print(num)
            No_Nvn -= 1
        num += 1
No_Nvn = int(input('Input: '))
N_Niven(No_Nvn)

# Generate between range of numbers
def Range_Niven(first,second):
    for num in range(first, second+1):
        sum=0
        c_num=num
        while num!=0:
            rem=num%10
            sum+=rem
            num//=10
        if c_num%sum==0:
            print(c_num)

first=int(input('First: '))
second=int(input('Second: '))
Range_Niven(first,second)