# a
# ab
# abc
# abcd
# abcde
S='abcde'
for ev in range(len(S)):
    for ch in range(ev+1):
        print(S[ch],end='')
    print()




# Using Slice
S = 'abcde'
for i in range(1, len(S) + 1):
    print(S[:i])