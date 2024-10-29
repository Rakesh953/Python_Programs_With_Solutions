# Composite Number
compo = lambda num:len([val for val in range(1,num+1) if num%val==0])>2
print(compo(6))