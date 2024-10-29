S='Engineering'
count=0
for ch in S:
    if ch in 'AEIOUaeiou':
        count+=1
print(count)