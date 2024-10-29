num = int(input('Enter the number: '))
c_num = num**2
sum=0
while c_num!=0:
    rem=c_num%10
    sum=rem+sum
    c_num//=10
if num==sum:
    print('Neon number')
else:
    print('not a neon number')