def Factorial(num,F=1):
    for n in range(1,num+1):
        F*=n
    return F
print(Factorial(4))