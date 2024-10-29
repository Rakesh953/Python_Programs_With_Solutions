def Pronic(num):
    for n in range(num+1):
        if n*(n+1)==num:
            return True
    else:
        return False
num=int(input('Enter the number: '))
print(Pronic(num))



# First N numbers 
def N_Pronic(No_P,num=0):
    while No_P!=0:
        for n in range(0,num+1):
            if n*(n+1)==num:
                print(num)
                No_P-=1
                break
        num+=1
No_P=int(input('Input: '))
N_Pronic(No_P)



# Generate between range of numbers
def Range_Pronic(first,second):
    for num in range(first,second+1):
        for n in range(0,num+1):
            if n*(n+1)==num:
                print(num)
                break
first=int(input('First: '))
second=int(input('Second: '))
Range_Pronic(first,second)