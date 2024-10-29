d={num for num in range(2,7) if num%2==0}
print(d)

d={num:num for num in range(2,7) if num%2==0}
print(d)

d={num:num*2 for num in range(2,7) if num%2!=0}
print(d)

d={num:num*2 for num in range(2,7) if num%2!=0}
print(d)

s='We are engineer'
l=s.split()
d={word for word in l}
print(d)

s='We are engineer'
l=s.split()
d={word:len(word) for word in l}
print(d)