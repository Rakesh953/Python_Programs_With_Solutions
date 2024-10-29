def Composite(num, count=0):
    for n in range(1,num+1):
        if num%n==0:
            count+=1
    return count>2
num=int(input('Enter the number: '))
print(Composite(num))

# First N numbers
def N_Composite(No_P,num=0):
    while No_P!=0:
        Count=0
        for n in range(1,num+1):
            if num%n==0:
                Count+=1
        if Count>2:
            print(num)
            No_P-=1
        num+=1
No_P=int(input('Input: '))
N_Composite(No_P)