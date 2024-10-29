composite=list(filter(lambda num:len([val for val in range(1,num+1) if num%val==0])>2, [2,3,4,5,6,7,8]))
print(composite)