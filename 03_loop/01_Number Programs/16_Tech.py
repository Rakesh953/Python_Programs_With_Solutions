num=int(input('Enter the number: '))
c_num=num
half=10**(len(str(num))//2)
LF=num%half
FH=num//half
if (LF+FH)**2==c_num:
    print('Tech number')
else:
    print('Not a tech number')
