def Spy(num,sum=0,product=1):
    while num!=0:
        rem=num%10
        sum+=rem
        product*=rem
        num//=10
    return sum==product
num=int(input('Enter The number: '))
print(Spy(num))