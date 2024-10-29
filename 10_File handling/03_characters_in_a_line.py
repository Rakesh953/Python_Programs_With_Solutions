file = 'D:\\Study\\PySpider\\Python\\Programming\\10_File handling\\rakesh.txt'

with open(file, 'r') as F:
    count = sum(1 for line in F if len(line.strip()) == 6)

print(f'The file has {count} lines with exactly 6 characters.')
