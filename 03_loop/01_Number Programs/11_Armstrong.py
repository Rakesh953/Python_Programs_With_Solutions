num = int(input('Enter the number: '))
c_num = num  
sum = 0
pwr = len(str(num))
while num != 0:
    rem = num % 10
    sum += rem ** pwr
    num //= 10
if c_num == sum:
    print(c_num, 'is an Armstrong Number')
else:
    print(c_num, 'is not an Armstrong number \n because the sum of the digits raised to the power', pwr, 'is', sum)
