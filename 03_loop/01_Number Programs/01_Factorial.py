# calculate the number
num=int(input('Enter the number:'))
ans=1
for val in range(1,num+1):
    ans=ans*val # or ans*=val
print(ans)



# First N numbers
LN=int(input('Enter the range number: '))
for num in range(1,LN+1):
    Fact=1
    for val in range(1,num+1):
        Fact*=val
    print(f"Factorial of {num} is {Fact}")



# Generate between range of numbers
FN=int(input('Enter the starting number: '))
LN=int(input('Enter the last number: '))
for num in range(FN,LN+1):
    Fact=1
    for val in range(1,num+1):
        Fact*=val
    print(f"Factorial of {num} is {Fact}")