num=int(input('Enter the number: '))
copy=num
sum=0

while num!=0:
    rem=num%10
    sum+=rem
    num//=10
if copy%sum==0:
    print('Niven number')
else:
    print('Not a Niven number')


