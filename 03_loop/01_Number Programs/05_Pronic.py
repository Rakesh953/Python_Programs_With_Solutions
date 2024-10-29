num=int(input('Enter the number: '))
for n in range(0,(num//2)+1):
    if n*(n+1)==num:
        print('Pronic Number')
        break
else:
    print('Not a pronic number')

# # Using while loop 
# num=int(input('Enter the number: '))
# n=0
# while(n*(n+1)<=num):
#     if (n*(n+1)==num):
#         print('Pronic number')
#         break
#     else:
#         n=n+1
# else:
#     print('Not a pronic number')