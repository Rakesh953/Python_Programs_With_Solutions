num = int(input('Enter the number: '))
c_num = num  
sum = 0
pwr = len(str(num))
while num != 0:
    # print(pwr,'\n')  # \To check the the len digit
    rem = num % 10
    sum += rem ** pwr
    num //= 10
    pwr-=1
if c_num == sum:
    print('Disarium Number')
else:
    print('Not a disarium number')
