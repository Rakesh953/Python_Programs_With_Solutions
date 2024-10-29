# Multiply with next character
s='abcd'
newL=[ch*2 for ch in s]
print(newL)


# Even ANSII numbers 
s='abcd'
newL=[ch for ch in s if ord(ch)%2==0]
print(newL)


# Print 10 to 15
num=[val for val in range(10,16)]
print(num)

# *
# **
# ***
# ****
# *****
L=['*'*st for st in range(1,6)]
print('\n'.join(L))


#Print Even Number from given List 
l=[2,3,4,5,6,7,8,9]
newL=[num for num in l if num%2==0]
print(newL)

# Print Odd Number from given List 
l=[2,3,4,5,6,7,8,9]
newL=[num for num in l if num%2!=0]
print(newL)


# print odd number in decending order and even number in accending order
    # inpute like - [14,19,18,16,25,27,11]
    # Output -      [27,25,19,11,14,16,18]
L=[14,19,18,16,25,27,11]
evn=[num for num in L if num%2==0]
odd=[num for num in L if num%2!=0]
newevn=sorted(evn)
newodd=sorted(odd ,reverse=True)
print(newodd+newevn)

#       Or

L=[14,19,18,16,25,27,11]
evn=[num for num in L if num%2==0]
odd=[num for num in L if num%2!=0]
evn.sort()
odd.sort(reverse=True)
print(odd+evn)





L=[2,4,6,9,0,3,0,2,6,0,2,0]
# Output - [2, 4, 6, 9, 3, 2, 6, 2, 0, 0, 0, 0]
n1=[num for num in L if num!=0]
n2=[num for num in L if num==0]
print(n1+n2)

#       or

L=[2,4,6,9,0,3,0,2,6,0,2,0]
newl=[num for num in L if num!=0]+[0]*L.count(0)
print(newl)

        # or 

L = [2, 4, 6, 9, 0, 3, 0, 2, 6, 0, 2, 0]
# Count the number of zeros in the original list L
num_zeros = L.count(0)
# Create a new list without the zeros, and then append the appropriate number of zeros at the end
newl = [num for num in L if num != 0] + [0] * num_zeros
print(newl)




s1='abc'
s2='mn'
for ch1 in s1:
    for ch2 in s2:
        print(ch1+ch2)
        #or
s1='abc'
s2='mn'
newl=[ch1+ch2 for ch1 in s1 for ch2 in s2]
print(newl)




# L=[2,3,5,1,4,7]
# Target=6
# newL=[L[ind1],L[ind2] for ind in range(ind1-10),for ind2 in range(ind+1) L[ind1]l[indd2]]
# print(newL)

L = [2, 3, 5, 1, 4, 7]
Target = 6
newL = [(L[ind1], L[ind2]) for ind1 in range(len(L)) for ind2 in range(ind1 + 1) if L[ind1] + L[ind2] == Target]
print(newL)

