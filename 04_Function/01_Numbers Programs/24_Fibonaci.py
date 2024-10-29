def Fibonacci(F,S,Number):
    for i in range(1,Number+1):
        print(F)
        temp=F
        F=S
        S+=temp
F=int(input('First number: '))
S=int(input('Second number: '))
Number=int(input('How many Fibonacci number you want: '))
Fibonacci(F,S,Number)