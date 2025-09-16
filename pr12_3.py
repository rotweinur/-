text=input()
a=[]
for i in range(len(text)-1):
    a+=text[i]
print(len(set(a)))