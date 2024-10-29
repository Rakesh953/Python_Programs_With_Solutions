def Disarium(num,c_num,power,sum=0):
    while num!=0:
        rem=num%10
        sum+=rem**power
        num//=10
        power-=1
    return c_num==sum
num=int(input('Enter the Number: '))
print(Disarium(num,c_num=num,power=(len(str(num)))))