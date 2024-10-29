def Odd(svo,evo):
    if svo%2!=0:
        print(svo)
    if svo==evo:
        return
    Odd(svo+1,evo)
svo=int(input('Starting value: '))
evo=int(input('Ending Value: '))
Odd(svo,evo)