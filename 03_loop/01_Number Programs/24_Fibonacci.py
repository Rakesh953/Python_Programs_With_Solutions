F=int(input('First number: '))
S=int(input('Second number: '))
N=int(input('How many Fibonacci number you want to generate:'))
for i in range(1,N+1):
    print(F)
    # Temp=F
    # F=S
    # S+=Temp
    # or 
    F, S = S, F +S