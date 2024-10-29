# # print longest word in the given file

# file = r'D:\Study\PySpider\Python\Programming\10_File handling\rakesh.txt'

# with open(file, 'r') as F:
#     longest_word = ''
#     for line in F:
#         words = line.split()  # Split the line into words
#         for word in words:
#             # Update longest_word if the current word is longer
#             if len(word) > len(longest_word):
#                 longest_word = word

# print(f'The longest word in the file is: "{longest_word}" with {len(longest_word)} characters.')


file = r'D:\Study\PySpider\Python\Programming\10_File handling\rakesh.txt'

with open(file, 'r') as F:
    longest_word = max((word for line in F for word in line.split()), key=len, default='')

print(f'The longest word in the file is: "{longest_word}" with {len(longest_word)} characters.')
