num=int(input('Enter the number: '))
count=0
c_num=num
rev=0
for n in range(1,num+1):
    if num%n==0:
        count+=1
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num//=10
if count==2 and c_num==rev:
    print(c_num,'is a PaliPrime Number')
else:
    print(c_num,'is not a PaliPrime Number')