# S='2a3d4a1d'   # Output - aadddaaaad
# n=len(S)
# res=''
# for ind in range(0,n-1,2):
#     res+=int(S[ind])*S[ind+1]
# print(res)



S='aadddaaaabbccc'   #Output - 2a3d4a2b3c
S += ''  # Add an extra character to avoid index out of range error
n = len(S)
count = 1
res = ''  # Initialize res to hold the result

for ind in range(n - 1):
    if S[ind] == S[ind + 1]:
        count += 1
    else:
        res += str(count) + S[ind]  # Append count and character
        count = 1  # Reset count for the next sequence

# The last sequence should be added after the loop
print(res)
