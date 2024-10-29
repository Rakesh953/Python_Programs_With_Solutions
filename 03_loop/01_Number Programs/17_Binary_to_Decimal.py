binaary=int(input('Enter Binary digits: '))
p=1
sum=0
while binaary!=0:
    rem=binaary%10
    if rem!=0 and rem!=1:
        print('Enter Binary digits only')
        break
    sum+=rem*p
    p*=2
    binaary//=10
else:
    print(sum)