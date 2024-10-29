def Count_Digits(num,Count=0):
    while num!=0:
        rem=num%10
        Count+=1
        num//=10
    return Count
num=int(input('Input: '))
print(Count_Digits(num))