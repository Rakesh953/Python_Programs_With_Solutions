# S='aadddaaaabbccc'  #Output - 4
S = 'aadddaaaabbccc'
count = 0  # Initialize the count

# Traverse the string and count distinct blocks of characters
for i in range(len(S)):
    if i == 0 or S[i] != S[i - 1]:  # Check if the current character is different from the previous one
        count += 1  # Increase the count for a new block

print(count)


