text=input().split()
new=[]
for i in range(len(text)-1):
    new.append(len(text[i]))
print(min(new))