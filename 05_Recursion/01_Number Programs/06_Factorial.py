def Factorial(num):
    if num==0 or num==1:
        return 1
    return num * Factorial(num-1)
num=int(input('Enter the number: '))
print(Factorial(num))