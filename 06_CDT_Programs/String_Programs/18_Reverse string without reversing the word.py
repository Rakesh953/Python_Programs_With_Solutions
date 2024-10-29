# S='hey how are you'
# L=S.split()
# RevL=L[::-1]
# print(' '.join(RevL))

S = 'hey how are you'
L = S.split()
RevL = []
for i in range(len(L) - 1, -1, -1):
    RevL.append(L[i])
print(' '.join(RevL))








# # without using inbuilt method

# S = 'hey how are you'
# L = S.split()  # Split the string into a list of words
# RevS = ''  # Initialize an empty string to hold the reversed sentence

# # Manually reverse the order of words
# for i in range(len(L) - 1, -1, -1):
#     RevS += L[i]  # Add each word in reverse order
#     if i > 0:  # Add space between words
#         RevS += ' '
# print(RevS)

S = 'hey how are you'
word=''
res=''
for ch in S:
    if ch==' ':
        res=' '+word+res
        word=''
    else:
        word=word+ch
print(word+res)