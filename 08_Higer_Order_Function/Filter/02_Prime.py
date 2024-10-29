# to find prime numbers of given list [3,7,8,10,17,19,20]
f=list(filter(lambda num: len([val for val in range(1,num+1) if num % val==0])==2,[3,7,8,10,17,19,20]))
print(f)






# # Taking a list of numbers as input
# nums = list(map(int, input('Enter the numbers separated by space: ').split()))
# prime = list(filter(lambda num: len([val for val in range(1, num + 1) if num % val == 0]) == 2, nums))
# print(prime)





# # Find the prime numbers upto that number
# num = int(input('Enter the number: '))
# prime = list(filter(lambda num: len([val for val in range(1, num + 1) if num % val == 0]) == 2, range(1, num + 1)))
# print(prime)

