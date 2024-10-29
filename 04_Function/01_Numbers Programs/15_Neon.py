def Neon(num,n,sum=0):
    while n!=0:
        rem=n%10
        sum+=rem
        n//=10
    return num==sum
num=int(input('Input: '))
print(Neon(num,n=num**2))