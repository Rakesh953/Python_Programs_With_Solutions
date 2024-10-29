num=int(input('Enter the number: '))
print('Composite' if len([val for val in range(1,num+1) if num%val==0 ])>2 else 'Not Composite')