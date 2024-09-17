word = input("Введите слово: ")
letter = input("Введите букву: ")

count = 0

for char in word:
    if char == letter:
        count += 1

print(f"Буква '{letter}' встречается в слове '{word}' {count} раз(а).")