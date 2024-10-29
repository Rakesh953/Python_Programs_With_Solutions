def Sunny(num):
    for n in range(1,num+1):
        if n**2==num+1:
            return True
    return False
num=int(input('Enter the Number:'))
print(Sunny(num))

# # while loop
# def Sunny(num,n=1):
#     while n**2<=(num+1):
#         if n**2==num+1:
#             return True
#         n+=1
#     return False
# num=int(input('Enter The number: '))
# print(Sunny(num))
    
# First N numbers 
def N_Sunny(No_P,num=0):
    while No_P!=0:
        for n in range(1,num+1):
            if n**2==num+1:
                print(num,end=',')
                No_P-=1
                break
        num+=1
No_P=int(input('How many Sunny Number you want: '))
N_Sunny(No_P)

# Generate between range of numbers
def Range_Sunny(First,Second):
    for num in range(First,Second+1):
        for n in range(1,num+1):
            if n**2==num+1:
                print(num)
                break
            
First=int(input('First: '))
Second=int(input('Second: '))
Range_Sunny(First,Second)