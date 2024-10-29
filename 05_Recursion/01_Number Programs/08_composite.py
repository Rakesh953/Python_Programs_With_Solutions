def Composite(num,div=1,count=0):
    if div>num:
        return count>2
    if num%div==0:
        count+=1
    return Composite(num,div+1,count)
num=int(input('Enter the number: '))
print(Composite(num))