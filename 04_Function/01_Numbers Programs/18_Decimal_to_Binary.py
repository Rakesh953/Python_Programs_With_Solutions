def Decimal(num,p=1,res=0):
    while num!=0:
        rem=num%2
        res+=rem*p
        p*=10
        num//=2
    return res
num=int(input('Enter the Ddecimal Value: '))
print(Decimal(num))