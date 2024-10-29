filename = 'D:\\Study\\PySpider\\Python\\Programming\\10_File handling\\rakesh.txt'
with open(filename, 'r') as file:
    data = file.read()  # Read the entire file
    words = data.split()  # Split the data into words
    num_words = len(words)  # Count the number of words
print(f'The file has {num_words} words.')