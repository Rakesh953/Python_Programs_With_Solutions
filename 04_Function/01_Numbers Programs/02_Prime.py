################################################################################
# ---------------------------------------------------------------------------------
# # Function without Arguments and without Return Type
# def check_prime():
#     num = int(input('Enter a number: '))
#     count = 0
#     for val in range(1, num + 1):
#         if num % val == 0:
#             count += 1
#     if count == 2:
#         print(f"{num} is a Prime number")
#     else:
#         print(f"{num} is Not a prime number")

# # Call the function
# check_prime()
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
# # Function with Arguments and without Return Type
# def check_prime_with_args(num,count = 0):
#     for val in range(1, num + 1):
#         if num % val == 0:
#             count += 1
#     if count == 2:
#         print(f"{num} is a Prime number")
#     else:
#         print(f"{num} is Not a prime number")

# # Example usage
# num = int(input('Enter a number: '))
# check_prime_with_args(num)
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
# # Function without Arguments and with Return Type
# def check_prime_and_return():
#     num = int(input('Enter a number: '))
#     count = 0
#     for val in range(1, num + 1):
#         if num % val == 0:
#             count += 1
#     if count == 2:
#         return f"{num} is a Prime number"
#     else:
#         return f"{num} is Not a prime number"

# # Call the function and print the result
# result = check_prime_and_return()
# print(result)
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
# # Function with Arguments and with Return Type
# def check_prime_with_args_and_return(num, count = 0):
#     for val in range(1, num + 1):
#         if num % val == 0:
#             count += 1
#     return f"{num} is a Prime number" if count == 2 else f"{num} is Not a prime number"

# # Example usage
# num = int(input('Enter a number: '))
# result = check_prime_with_args_and_return(num)
# print(result)
# --------------------------------------------------------------------------------------
############################################################################################





def Prime(num,count=0): 
    for n in range(1,num+1):
        if num%n==0:
            count+=1
    return count==2
num=int(input('Enter the number: '))
print(Prime(num)) 

# First N numbers 
def N_Prime(No_P,num=0):
    while No_P!=0:
        Count=0
        for n in range(1,num+1):
            if num%n==0:
                Count+=1
        if Count==2:
            print(num)
            No_P-=1
        num+=1
No_P=int(input('Input: '))
N_Prime(No_P)


# First N numbers



# #  Prime Number without count variable
# def Prime(num):
#     if num < 2:
#         print("Not prime")
#         return
#     for val in range(2, num):
#         if num % val == 0: # If num is divisible by any number val in this range, then num is not a prime number.
#             print("Not prime")
#             return
#     print("Prime")
# num = int(input('Enter a number: '))
# Prime(num)
#             # OR 
# def Prime(num):
#     if num < 2:
#         return False
#     for val in range(2, num):
#         if num % val == 0: # If num is divisible by any number val in this range, then num is not a prime number.
#             return False
#     return True
# num = int(input('Enter a number: '))
# print(Prime(num))