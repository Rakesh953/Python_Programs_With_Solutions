num = int(input('Input: '))
while num % 2 == 0:
    num //= 2
while num % 3 == 0:
    num //= 3
while num % 5 == 0:
    num //= 5

if num == 1:
    print('Ugly number')
else:
    print('Not an Ugly number')


