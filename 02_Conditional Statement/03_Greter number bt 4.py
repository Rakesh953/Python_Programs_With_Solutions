A=int(input("Enter 1st number:"))
B=int(input("Enter 2nd number:"))
C=int(input("Enter 3rd number:"))
D=int(input("Enter 4th number:"))

# if A>B:
#     if A>C:
#         if A>D:
#             print(A)
#         else:
#             print(D)
#     else:
#         if C>D:
#             print(C)
#         else:
#             print(D)

# else:
#     if B>C:
#         if B>D:
#             print(B)
#         else:
#             print(D)
#     else:
#         if C>D:
#             print(D)

# or 

if A>B and A>C and A>D:
    print(A)
elif B>C and B>D and B>A:
    print(B)
elif C>D and C>A and C>B:
    print(C)
else:
    print(D)
