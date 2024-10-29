def Binary(num,sum=0,p=1):
    while num!=0:
        rem=num%10
        if rem != 0 and rem != 1:
            return 'Enter Binary Digits Only'
        sum+=rem*p
        p*=2
        num//=10
    return sum
num=int(input('Input: '))
print(Binary(num))


def Binary_D(digits,res=0,p=1):
    while digits!=0:
        last_d=digits%10
        if last_d!=0 and last_d!=1:
            return 'Enter the binary digits Only'
        res+=last_d*p
        p*=2
        digits//=10
    return res
digits=int(input('Input: '))
print(Binary_D(digits))