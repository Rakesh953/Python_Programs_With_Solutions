# num=int(input('Enter the number: '))
# res=len([val for val in range(1,num+1) if num%val==0])
# print('prime' if res==2 else 'not prime')


num = int(input('Enter the number: '))
print('prime' if len([val for val in range(1, num + 1) if num % val == 0]) == 2 else 'not prime')
