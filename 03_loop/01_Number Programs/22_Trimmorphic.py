num=int(input('Input: '))
cube=num**3
last_Digit=cube%10**(len(str(num)))
if num==last_Digit:
    print('Trimorphic')
else:
    print('Not Trimorphic')