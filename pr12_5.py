t1=input()
t2=input()
t3=input()
a=set()
for i in t1+t2+t3:
    if (i in t1)+(i in t2)+(i in t3)==1 and i not in a:
        a.add(i)
print(a)