def Power(num,p):
    if p==0:
        return 1
    return num*Power(num,p-1)
print(Power(2,2))