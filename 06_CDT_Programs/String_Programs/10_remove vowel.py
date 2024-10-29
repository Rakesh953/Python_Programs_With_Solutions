# S='Engineering'
# for ch in S:
#     if ch in 'AEIOUaeiou':
#         continue
#     print(ch)

S='Engineering'
vwl='AEIOUaeiou'
res=''
for ch in S:
    if ch not in vwl:
        res+=ch
print(res)



