# L=[12,13,14,15]
# m=max(L, key=lambda num:[num%5])
# print(m)

# s='we are in hunger of job'
# l=s.split()
# m=max(l,key=len)
# print(m)

s='engineering'
m=max(s,key=lambda ch:[s.count(ch)])
print(m)

# print key in dictonary which is having the highest value
d={'a':100,'n':20,'b':30,'d':45}
L=max(d)
print(L)    #It finding the highest valeu of key(in ANSII Value)


d={'a':100,'m':1011, 'n':20, 'b':30, 'd':45}
L=max(d,key=lambda dt:[d[dt],dt])
print(L)