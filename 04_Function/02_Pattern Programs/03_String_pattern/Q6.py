# abcde
# abcd
# abc
# ab
# a

S='abcde'
for ev in range(len(S),0,-1):
    for ch in range(ev):
        print(S[ch],end='')
    print()

S = 'abcde'
for ev in range(len(S), 0, -1):
    # print(ev)
    print(S[:ev])
