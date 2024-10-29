def Emirp(num,c_num,rev=0,count=0,count1=0):
    for n in range(1,num+1):
        if num%n==0:
            count+=1
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    for n1 in range(1,rev+1):
        if rev%n1==0:
            count1+=1
    return count==2 and count1==2 and c_num!=rev
num=int(input('Enter the number: '))
print(Emirp(num,c_num=num))