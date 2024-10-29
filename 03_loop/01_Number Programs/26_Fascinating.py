num=int(input('Input: '))
con_Fasc=''
for i in range(1,4):
    Fasc=num*i
    con_Fasc+=str(Fasc)
if sorted(con_Fasc) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    print(f'{num} is a Fascinating number')
else:
    print(f'{num} is not a Fascinating number')





# # to sort the number  
# sd=sorted(str(con_Fasc))
# sn=int(''.join(sd))
# # print(sn)
# # print(type(sn))
# if sn==123456789:
#     print('Fascinating number')
# else:
#     print('Not Facinnating  number')