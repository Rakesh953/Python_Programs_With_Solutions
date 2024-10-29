# Number of terms in the Fibonacci series
n =int(input('Enter the number: '))  # You can change this to generate more or fewer terms

# Initialize the first two Fibonacci numbers
a = 0
b = 1

# Print the first Fibonacci number
print(a)

# Print the second Fibonacci number if n is greater than 1
if n > 1:
    print(b)

# Generate the rest of the Fibonacci series
i = 2
while i < n:
    next_number = a + b
    print(next_number)
    
    # Update the values for the next iteration
    a = b
    b = next_number
    
    i += 1
