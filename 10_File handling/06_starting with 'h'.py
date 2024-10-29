file = r'D:\Study\PySpider\Python\Programming\10_File handling\rakesh.txt'

with open(file, 'r') as F:
    h_words = [word for line in F for word in line.split() if word.lower().startswith('h')]

print('Words starting with "h":', h_words)