words=input().split()
first = words[0]
result = []

for word in words:
    if word != first and len(word) == len(set(word)):
        result.append(word)

print(result)