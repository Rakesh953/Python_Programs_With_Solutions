factor=lambda num:list(filter(lambda fa:num%fa==0, range(1,num+1)))
print(factor(14))
print(factor(7))