# # Using Slicing 
# L=[1,2,3,4]
# print(L[::-1])



# Without Slice
L=[1,2,3,4]
RL=[]
for i in range(len(L)-1,-1,-1):
    RL.append(L[i])
print(L)
print(RL)




# # Using Function 
# def RevL(L):
#     RL=[]
#     for i in range(len(L)-1,-1,-1):
#         RL.append(L[i])
#     return RL
# L=[1,2,3,4]
# print(RevL(L))




# # Taking input from the user 
# def RevL(L):
#     RL = []
#     for i in range(len(L) - 1, -1, -1):
#         RL.append(L[i])
#     return RL
# L = list(map(int, input('Enter a list of numbers (space-separated): ').split()))
# print('Reversed list:', RevL(L))




# # reverse the given list without creating a new list in existing memory location
# L = [1, 2, 3, 4]
# n = len(L)
# for i in range(n // 2):
#     L[i], L[n - i - 1] = L[n - i - 1], L[i]
# print('Reversed list:', L)