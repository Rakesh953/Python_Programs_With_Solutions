S = 'Rakesh, Krishna, Madhu, Radha, Rakesh, Radha'
words = S.split(', ')
WC={}
for word in words:
    if word in WC:
        WC[word] += 1
    else:
        WC[word] = 1
for word, count in WC.items():
    print(f'{word} = {count}')
