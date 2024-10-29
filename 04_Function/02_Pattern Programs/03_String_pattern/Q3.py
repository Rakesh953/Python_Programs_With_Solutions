S = 'abcde'
rev = S[::-1]  # Using slice to reverse the string
space = 4
count = 1

for i in range(1, len(rev) + 1):
    print(' ' * space, rev[i-1] * count, sep='')
    space -= 1
    count += 1


# S='abcde'
# rev=''
# space=4
# count=1
# for ch in S:
#     rev=ch+rev
# for i in rev:
#     print(' '*space, i*count, sep='')
#     space-=1
#     count+=1

