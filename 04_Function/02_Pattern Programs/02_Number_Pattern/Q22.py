# space=4
# for ev in range(0,5):
#     print(' '*space, end='')
#     for num in range(1,ev+1):
#         print(num,end='')
#     space-=1
#     print()

# for sv in range(1,4):
#     for num in range(sv,0,-1):
#         print(num,end='')
#     print()


space = 4
for ev in range(1, 5):
    print(' ' * (space - ev), end='')  # Adjust the spaces
    for num in range(1, ev + 1):       # Incrementing part
        print(num, end='')
    for num in range(ev - 1, 0, -1):   # Decrementing part
        print(num, end='')
    print()                            # Move to the next line
