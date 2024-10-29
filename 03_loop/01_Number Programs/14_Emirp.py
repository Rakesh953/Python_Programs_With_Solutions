num=int(input('Enter the Number: '))
c_num=num
rev=0
count=0
count1=0
for n in range(1,num+1):
    if num%n==0:
        count+=1
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num//=10
for n1 in range(1,rev+1):
    if rev%n1==0:
        count1+=1
if count==2 and count1==2 and c_num!=rev:
    print('Emirp Number')
else:
    print('Not Emirp')



# anathor Way
num = int(input('Enter the Number: '))
copy = num  # Store original number
rev = 0
count = 0
count1 = 0

# Check if the original number is prime
for n in range(1, num + 1):
    if num % n == 0:
        count += 1

# Reverse the number
while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

# Check if the reversed number is prime
for n1 in range(1, rev + 1):
    if rev % n1 == 0:
        count1 += 1

# Check if both the original and reversed numbers are prime and not a palindrome
if (copy != rev) and (count == 2) and (count1 == 2):
    print('Emirp Number')
else:
    print('Not Emirp')
