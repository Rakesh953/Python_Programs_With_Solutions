N = 123456
c = len(str(N))
print(c)


# Without Inbuilt
N = 1239
c = 0
while N > 0:
    N = N // 10  
    c += 1      
print(c)