def name(n='Rakesh',i=0):
    if i==10:
        return
    print(n)
    name(n,i+1)
name()

    # or 

# count=1
# def printer(name):
#     global count
#     if count<=10:
#         print(name)
#         count+=1
#         printer(name)
# printer('Rakesh')
