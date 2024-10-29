file = r'D:\Study\PySpider\Python\Programming\10_File handling\rakesh.txt'

with open(file, 'r') as F:
    longest_line = max(F, key=len, default='')

print(f'The longest line in the file is:\n "{longest_line.strip()}"\n  with: {len(longest_line)} characters.')
