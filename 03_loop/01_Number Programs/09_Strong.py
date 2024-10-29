num=int(input('Enter a number: '))
copy=num
F_sum=0
while num!=0:
    rem=num%10 # To Extract last Digit from given number
    Factor=1
    for val in range(1,rem+1):
        Factor=Factor*val
    F_sum=F_sum+Factor
    num//=10 # To remove last one digit from the given number
if copy==F_sum:
    print('Strong number')
else:
    print('Not a Strong Number')
