S='hey how are you'
L=S.split()
NewL=[]
for word in L:

# Without slice
    # rev = ''
    # for ch in word:
    #     rev+=ch  # Build the reversed word by prepending characters

# With slice
    rev=word[::-1]

    NewL.append(rev)
print(' '.join(NewL))



# without using inbuilt method
S = 'hey how are you'
word=''
res=''
for ch in S:
    if ch==' ':
        res=res+word+' '
        word=''
    else:
        word=ch+word
print(res+word)