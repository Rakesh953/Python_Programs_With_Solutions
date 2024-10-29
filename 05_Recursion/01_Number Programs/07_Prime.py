def Prime(num, div=1, count=0):
    if div > num:
        return count == 2
    if num % div == 0:
        count += 1
    return Prime(num, div + 1, count)
print(Prime(3)) 

# # With out counting the divisior
# def is_prime(num, val=2):
#     if num < 2:
#         return False
#     if val * val > num:   # this is nothing but to check halp of the given number
#         return True
#     if num % val == 0:
#         return False
#     return is_prime(num, val + 1)
# num = int(input('Enter a number: '))
# print(is_prime(num))