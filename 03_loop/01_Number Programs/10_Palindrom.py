num=int(input('Enter the number: '))
copy_num=num
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if copy_num==rev:
    print(rev,'is a plindrom Number')
else:
    print(copy_num,'is not a Palindrom number because the reverse number is',rev)