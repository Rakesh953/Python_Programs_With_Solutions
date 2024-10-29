# S='Engineering'
# ans=''
# for ch in S:
#     if ch not in 'AEIOUaeiou':
#         ans+=ch
# print(ans)

S = 'Engineering'
for ch in S:
    if ch not in 'AEIOUaeiou':
        print(ch, end='')
