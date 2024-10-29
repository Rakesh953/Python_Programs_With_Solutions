L = [12, 11, 13, 14, 12, 13, 15, 16, 12, 13, 15, 17, 16, 19]
# Initialize sums and products
sum_odd = 0
sum_even = 0
product_odd = 1
product_even = 1

# Iterate through the list
for n in L:
    if n % 2 == 0:  # Even value
        sum_even += n
        product_even *= n
    else:  # Odd value
        sum_odd += n
        product_odd *= n

# Output the results
print(f"Sum of even values: {sum_even}")
print(f"Product of even values: {product_even}")
print(f"Sum of odd values: {sum_odd}")
print(f"Product of odd values: {product_odd}")
