prime=lambda num:len([val for val in range(1,num+1)if num%val==0])==2
print(prime(7))



num = int(input('Enter the number: '))
prime = lambda num: 'Prime' if len([val for val in range(1, num+1) if num % val == 0]) == 2 else 'Not Prime'
print(prime(num))