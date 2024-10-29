num=int(input('Input: '))
sqr=num**2
rem=sqr%(10**(len(str(num))))
if num==rem:
    print('Automorphic')
else:
    print('Not')