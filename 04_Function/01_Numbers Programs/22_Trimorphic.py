def Trimorphic(num,cube):
    res=cube%10**(len(str(num)))
    return num==res
num=int(input('Input: '))
print(Trimorphic(num,cube=num**3))