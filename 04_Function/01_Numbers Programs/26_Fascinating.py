def Fascinating(num,Con_Fasc=''):
    for i in range(1,4):
        Fasc=i*num
        Con_Fasc+=str(Fasc)
    return sorted(str(Con_Fasc))==['1','2','3','4','5','6','7','8','9']
num=int(input('Input: '))
print(Fascinating(num))