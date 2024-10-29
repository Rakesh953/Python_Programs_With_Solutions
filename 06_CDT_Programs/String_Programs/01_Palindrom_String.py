def reverse_String(PS):
    reverse_str = ''
    for i in range(len(PS) - 1, -1, -1):
        reverse_str += PS[i]
    return reverse_str
# # Using Slicing 
#     return PS[::-1]
PS = input('Enter the string: ')
print('Reversed String:',reverse_String(PS))
