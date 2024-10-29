file = r'D:\Study\PySpider\Python\Programming\10_File handling\rakesh.txt'

with open(file, 'r') as F:
    ten_char_words = [word for line in F for word in line.split() if len(word) == 10]

print('Words with exactly 10 characters:', ten_char_words)
