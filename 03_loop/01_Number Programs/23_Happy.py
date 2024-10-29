num = int(input('Input: '))
while num > 9:
    result = 0
    while num != 0:
        rem = num % 10
        num //= 10
        result += (rem**2)
    num = result
if num == 1:  
    print('Happy number')
else:
    print('Unhappy Number')
