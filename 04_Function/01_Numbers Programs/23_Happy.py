def Happy(num):
    while num>9:
        result=0
        while num!=0:
            rem=num%10
            num//=10
            result+=rem**2
        num=result
    return num==1
num=int(input('Input: '))
print(Happy(num))