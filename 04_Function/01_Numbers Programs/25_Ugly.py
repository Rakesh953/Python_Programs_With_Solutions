def Ugly(num):
    while num%2==0:
        num//=2
    while num%3==0:
        num//=3
    while num%5==0:
        num//=5
    return num==1
num=int(input('Input: '))
print(Ugly(num))
