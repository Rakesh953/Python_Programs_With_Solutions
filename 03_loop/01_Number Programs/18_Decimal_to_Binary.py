num=int(input('Enter the Decimal numbers: '))
pos=1
res=0
while num!=0:
    rem=num%2
    res+=rem*pos
    num//=2
    pos*=10
print(res)