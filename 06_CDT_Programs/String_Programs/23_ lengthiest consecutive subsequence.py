s = "aadddaaaabbccc"
Max_L = 0
Cur_L = 1
L_Sub = ""

for i in range(1, len(s)):
  if s[i] == s[i-1]:
    Cur_L += 1
  else:
    if Cur_L > Max_L:
      Max_L = Cur_L
      L_Sub = s[i-Cur_L:i]
    Cur_L = 1
# Check if the last subsequence is the longest
if Cur_L > Max_L:
  Max_L = Cur_L
  L_Sub = s[i-Cur_L+1:i+1]

print(L_Sub)  # Output: aaaa