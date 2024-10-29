from functools import reduce
binary = [1, 0, 1, 1]  # Represents 11 in decimal
decimal = reduce(lambda x, y: 2 * x + y, binary)
print(decimal)  # Output: 11