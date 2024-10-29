def Tech(num,c_num,Half):
    Last_H=num%Half
    First_H=num//Half
    return (Last_H+First_H)**2==c_num
num=int(input('Input: '))
print(Tech(num,c_num=num,Half=10**(len(str(num))//2)))