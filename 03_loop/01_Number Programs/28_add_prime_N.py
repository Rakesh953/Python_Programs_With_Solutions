PH = 9078895125
sum=0
while PH!=0:
    rem=PH%10
    count=0
    for num in range(1,rem+1):
        if rem%num==0:
            count+=1
    if count==2:
        sum+=rem
    PH//=10
print(sum)