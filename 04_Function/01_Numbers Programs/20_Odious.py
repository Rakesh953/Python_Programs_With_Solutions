def Odious(num,sum=0):
    while num!=0:
        rem=num%2
        sum+=rem
        num//=2
    return sum%2!=0
num=int(input('Input: '))
print(Odious(num))