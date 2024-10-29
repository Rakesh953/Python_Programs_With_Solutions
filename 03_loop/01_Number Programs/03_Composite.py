num=int(input('Enter a number:'))
count=0
for val in range(1,num+1):
    if num%val==0:
        count+=1
if count>2:
    print(val,'It is a composite number')
else:
    print(val,'It is not a composite number')



# First N number  
No_Comp=int(input('Input: '))
Comp_C=1
while No_Comp!=0:
    count=0
    for i in range(1,Comp_C+1):
        if Comp_C%i==0:
            count+=1
    if count>2:
        print(Comp_C)
        No_Comp-=1
    Comp_C+=1

# Generate between range of numbers
S_N=int(input('Starting Number: '))
L_N=int(input('Last Number: '))
for i in range(S_N,L_N+1):
    count=0
    for n in range(1,i+1):
        if i%n==0:
            count+=1
    if count>2:
        print(i)