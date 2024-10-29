# def Automorphic(num):
#     sqr=num**2
#     rem=sqr%10**(len(str(num)))
#     return num==rem
# num=int(input('Input: '))
# print(Automorphic(num))


def Automorphic(num,sqr):
    rem=sqr%10**(len(str(num)))
    return num==rem
num=int(input('Input: '))
print(Automorphic(num,sqr=num**2))