# S = 'i love to travel on Holidays'
# words = S.split() # Split the string into words
# longest_word = max(words, key=len) # Find the longest word
# print(longest_word)


# S = 'i love to travel on Holidays'
# words = S.split()
# longest_word = ""
# max_length = 0
# for word in words:
#     # Calculate the length of the current word
#     current_length = 0
#     for char in word:
#         current_length += 1
#     # Update longest_word if the current word is longer
#     if current_length > max_length:
#         longest_word = word
#         max_length = current_length
# print(f"The lengthiest word is: {longest_word}")


# S='i love to travel on Holidays'
# HW=0
# Split=S.split()
# NewL=[]
# for word in Split:
#     if len(word)>HW:
#         HW=len(word)
#     if word not in NewL:
#         NewL.append(word)
# for word in NewL:
#     if len(word)==HW:
#         print(word)

s='i love to travel on Holidays'  # hi this is python this is class this
words=s.split()
LW=''
c=0
for i in words:
    if len(i)>c:
        c=len(i)
        LW=i
print(LW)