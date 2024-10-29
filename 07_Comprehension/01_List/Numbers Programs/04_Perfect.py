num=int(input('Enter the number: '))
res=sum([val for val in range(1,(num//2)+1) if num%val==0])
print('perfect' if res==num else 'Not Perfect') 




















# # without sum() function
# num=int(input('Enter the number: '))
# res=[val for val in range(1,(num//2)+1) if num%val==0]
# sum=0
# for n in res:
#     sum+=n
# print('perfect' if sum==num else 'Not Perfect') 