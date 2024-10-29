S='are'
C_sum=0
for ch in S:
    C_sum+=ord(ch) - 96  
    #     # or 
    # C_sum+=ord(ch) - ord('a') + 1
print(C_sum)
