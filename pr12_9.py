text = input().split()
strs = set()
a = None
for str in text:
    if str in strs:
        a = str
        break
    strs.add(str)
print(a)