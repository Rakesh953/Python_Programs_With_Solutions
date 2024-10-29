filename = 'D:\\Study\\PySpider\\Python\\Programming\\10_File handling\\rakesh.txt'
with open(filename, 'r') as file:
    num_lines = sum(1 for line in file)
print(f'The file has {num_lines} lines.')
