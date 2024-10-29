# Get the value whose sum is = to the given targe
L=[10,2,3,7,4,1,6,9]
Target=10
for ind1 in range(len(L)):
    for ind2 in range(ind1+1,len(L)):
        if L[ind1]+L[ind2]==Target:
            print(L[ind1],L[ind2])

# reverse the value also
            # print(L[ind2],L[ind1])