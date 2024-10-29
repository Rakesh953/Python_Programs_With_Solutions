# S='abcde'
# rev=''
# for ch1 in S:
#     rev=ch1+rev
# for sv in range(len(rev)):
#     for ch in range(sv,len(rev)):
#         print(rev[ch],end='')
#     print()

S = 'abcde'
for i in range(1, len(S) + 1):
    print(S[-i:])

