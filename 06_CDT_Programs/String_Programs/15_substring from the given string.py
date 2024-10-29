S='ABC'
for ch in range(len(S)):
    for sch in range(ch+1, len(S)+1):
        print(S[ch:sch])

S='abc'
SubS=[]
for i in range(len(S)):
    for j in range(i+1,len(S)+1):
        SubS.append(S[i:j])
print(SubS)