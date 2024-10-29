# S='abcde'
# rev=''
# count=1
# for ch in S:
#     rev=ch+rev
# for st in rev:
#     print(st*count, sep='')
#     count+=1

# Using Slice
S='abcde'
rev=S[::-1]
count=1
for ch in rev:
    print(ch*count,sep='')
    count+=1
#     # or 
# for ch in range(1,len(rev)+1):
#     print(rev[ch-1]*count,sep='')
#     count+=1