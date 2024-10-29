# S='Engineering'
# res=''
# for ch in range(11):
#     if S[ch] not in res:
#         res=res+S[ch]
# print(res)

#    or 

S = 'ENGINEERING'
res = ''
for ch in S:
    if ch not in res:
        res += ch
print(res)