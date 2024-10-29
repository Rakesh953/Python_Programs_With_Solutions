num = int(input('Enter the number: '))
sum = 0
product = 1

while(num != 0):
    rem = num % 10  # Get the last digit
    sum = sum + rem  # Add the digit to the sum
    product = product * rem  # Multiply the digit to the product
    num = num // 10  # Remove the last digit

if(sum == product):
    print('Spy Number')
else:
    print('Not a Spy Number')




num = int(input('Enter the number: '))
copy = num  # Create a copy of the number to use in the for loop condition
sum = 0  # Initialize the variable to store the sum of the digits
product = 1  # Initialize the variable to store the product of the digits

# Loop to iterate over each digit of the number
# The range is set from 1 to copy+1 to simulate a range long enough to cover all digits, but we manually break out once num is reduced to 0.
for val in range(1, copy + 1):
    if num == 0:  # If the number becomes 0, all digits have been processed; exit the loop
        break
    rem = num % 10  # Get the last digit of the number (remainder when divided by 10)
    sum = sum + rem  # Add the last digit to the sum
    product = product * rem  # Multiply the last digit to the product
    num //= 10  # Remove the last digit from the number by performing integer division by 10

# After processing all digits, compare the sum and product
if sum == product:
    print('Spy number')  # If sum and product are equal, it's a Spy Number
else:
    print('Not a Spy number')  # If sum and product are not equal, it's not a Spy Number
