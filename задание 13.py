R_1=int(input())
R_2=int(input())
S_1=3.14159*(R_1^2)
S_2=3.14159*(R_2^2)
if R_2>R_1:
  print(S_2-S_1)
else:
  print(S_1-S_2)