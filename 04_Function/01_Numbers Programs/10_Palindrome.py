def Palindrome(num,c_num,sum=0):
    while num!=0:
        rem=num%10
        sum=sum*10+rem
        num//=10
    return c_num==sum
num=int(input('Enter The number: '))
print(Palindrome(num,c_num=num))