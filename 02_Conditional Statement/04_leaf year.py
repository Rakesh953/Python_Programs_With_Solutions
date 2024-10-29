Year=int(input('Enter the Year to check This year is Leap year or not:'))
# if Year%4==0 and Year%100!=0:
#     print('Leap year')
# elif Year%400==0:
#     print('Leap year')
# else:
#     print('Not a Leap year')

# or 
if Year%400==0 or Year%100!=0 and Year%4==0:
    print('Leap year')
else:
    print('Not a Leap year')