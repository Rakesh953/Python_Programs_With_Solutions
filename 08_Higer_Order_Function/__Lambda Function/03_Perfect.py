num = int(input('Enter the number: '))
Perfect = lambda num: sum([val for val in range(1, (num // 2) + 1) if num % val == 0])
print('Perfect' if Perfect(num) == num else 'Not Perfect')


