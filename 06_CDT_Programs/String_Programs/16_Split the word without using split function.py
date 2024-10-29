S = 'hey how are you'
res = []
word = ''
for ch in S:
    if ch != ' ':  # Collect characters for the current word
        word += ch
    else:
        if word:  # Append the word if it's not empty when a space is found
            res.append(word)
            word = ''  # Reset word for the next one
# Append the last word after the loop (since no space follows it)
if word:
    res.append(word)
print(res)






# Generate all possible substrings for each word in the given string S = 'hey how are you', including an empty string between the words.
S='hey how are you'
res=[]
word=''
for ch in S:
    if ch!=' ':
        word+=ch
    else:
        res.append(word)
        word=''
    res.append(word)
print(res)
