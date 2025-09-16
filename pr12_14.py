hint = input("подсказка: ")
word = input("слово: ").lower()

print("\n" * 25)

hidden = "*" * len(word)

while hidden != word:
    print(hint)
    print(hidden)
    guess = input("буква или слово: ").lower()

    if len(guess) == 1:
        hidden = "".join(
            guess if word[i] == guess else hidden[i]
            for i in range(len(word))
        )
    else:
        if guess == word:
            hidden = word
        else:
            print("проигрыш!")
            break

print(hidden)
if hidden == word:
    print("победа!")