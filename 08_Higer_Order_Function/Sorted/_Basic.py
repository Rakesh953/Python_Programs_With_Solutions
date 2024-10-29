# s='ENGINEERING' 
# L=sorted(s)
# print(L)
# # output:['E', 'E', 'E', 'G', 'G', 'I', 'I', 'N', 'N', 'N', 'R']


# s='ENGINEERING'
# L=sorted(s, key=lambda ch:[s.count(ch),ch])
# print(L)


# #arrange word to string according to its Length
# s='we are in hunger of job'
# l=sorted(s.split(),key=len)
# print(l)
# # Output - ['we', 'in', 'of', 'are', 'job', 'hunger']


# arrange the key in asc ord of doctonary according value
d={'a':100,'m':1011, 'n':20, 'b':30, 'd':45}
l=sorted(d,key=lambda k:d[k])
print(l)


# arrange the key in doctonary according value in decending order
d={'a':100,'m':1011, 'n':20, 'b':30, 'd':45}
l=sorted(d,key=lambda k:d[k],reverse=True)
print(l)