# # Add the numbers of Given range
# def Add(num):
#     if num==10:
#         return num
#     return num+Add(num+1)
# print(Add(1))


# import sys
# # Check the current recursion limit
# print("Current recursion limit:", sys.getrecursionlimit())

# # Set a new recursion limit
# sys.setrecursionlimit(2000)  # Increase the limit to 2000

# # Verify the new recursion limit
# print("New recursion limit:", sys.getrecursionlimit())

def Add(svn,evn):
    if svn==evn:
        return svn
    return (svn+Add(svn+1,evn))
    # It adds the current value of svn to the result of the recursive call Add(svn + 1, evn).
svn=int(input('Starting Value: '))
evn=int(input('Ending Value: '))
print(Add(svn,evn))