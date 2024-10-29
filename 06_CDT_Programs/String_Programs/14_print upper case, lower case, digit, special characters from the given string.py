S = 'Hello, World! 123 @#$%^&*()'
upper_case = ''
lower_case = ''
digits = ''
special_characters = ''
for ch in S:
    if ch.isupper():
        upper_case += ch
    elif ch.islower():
        lower_case += ch
    elif ch.isdigit():
        digits += ch
    else:
        special_characters += ch
print("Uppercase characters:", upper_case)
print("Lowercase characters:", lower_case)
print("Digits:", digits)
print("Special characters:", special_characters)


# # In function 
# def categorize_characters(s):
#     # Initialize empty strings to collect characters
#     upper_case = ''
#     lower_case = ''
#     digits = ''
#     special_characters = ''

#     # Iterate through each character in the string
#     for ch in s:
#         if ch.isupper():
#             upper_case += ch
#         elif ch.islower():
#             lower_case += ch
#         elif ch.isdigit():
#             digits += ch
#         else:
#             special_characters += ch

#     return upper_case, lower_case, digits, special_characters

# # Example usage
# S = 'Hello, World! 123 @#$%^&*()'
# upper_case, lower_case, digits, special_characters = categorize_characters(S)

# print("Uppercase characters:", upper_case)
# print("Lowercase characters:", lower_case)
# print("Digits:", digits)
# print("Special characters:", special_characters)

