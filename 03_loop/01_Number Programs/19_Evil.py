num=int(input('Input: '))
sum=0
while(num!=0):
    rem=num%2
    sum=sum+rem
    num//=2
if(sum%2==0):
    print('Evil Number')
else:
    print('Odious Number')