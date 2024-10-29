def Strong(num,c_num,sum=0):
    while num!=0:
        rem=num%10
        Fact=1
        for n in range(1,rem+1):
            Fact*=n
        sum+=Fact
        num//=10
    return c_num==sum
num=int(input('Enter the Number: '))
print(Strong(num,c_num=num))