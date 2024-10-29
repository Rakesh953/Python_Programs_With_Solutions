A=int(input("Enter the First Number:"))
B=int(input("Enter the First Number:"))
C=int(input("Enter the First Number:"))

# if A>B:
#     if A>C:
#         print(A)
#     else:
#         print(C)
# else:
#     if B>C:
#         print(B)
#     else:
#         print(C)

# or
if A>B and A>C:
    print(A)
elif B>C and B>A:
    print(B)
else:
    print(C)


