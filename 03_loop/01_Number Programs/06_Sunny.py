num=int(input('Enter the Number: '))
## using for loop
# for n in range(num+1):
#     if n**2==(num+1):
#         print('Sunny Number')
#         break
# else:
#     print('Not a sunny number')

## using while loop
n=1
while(n**2<=(num+1)):
    if(n**2==(num+1)):
        print('Sunny Numbers')
        break
    else:
        n=n+1
else:
    print('Not a sunny number')

# print(n)