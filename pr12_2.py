print("Введите текст:")
text = input()
a = 1 
b = 1   
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        a += 1
        b = max(a, b)
    else:
        a = 1

print(b)