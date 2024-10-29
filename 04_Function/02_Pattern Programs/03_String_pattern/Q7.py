S='abcde'
for sv in range(len(S)):
    for ch in range(sv,len(S)):
        print(S[ch],end='')
    print()

S = 'abcde'
for sv in range(len(S)):
    print(S[sv:])