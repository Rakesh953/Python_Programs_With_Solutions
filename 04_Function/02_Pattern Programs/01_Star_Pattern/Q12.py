def print_diamond_pattern(rows):
    # Upper half of the pattern
    for st0 in range(1, rows + 1):
        for st1 in range(1, 2 * rows):
            if st1 <= st0 or st1 >= 2 * rows - st0:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# print_diamond_pattern(4) 
    # Lower half of the pattern
    for st0 in range(rows - 1, 0, -1):
        for st1 in range(1, 2 * rows):
            if st1 <= st0 or st1 >= 2 * rows - st0:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# Example usage
print_diamond_pattern(4) 