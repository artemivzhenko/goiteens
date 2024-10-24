surname = input("Введите вашу фамилию: ")

letter_frequency = {}
for letter in surname:
    if letter.isalpha():
        letter = letter.lower()
        letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

most_frequent_letter = max(letter_frequency, key=letter_frequency.get)

print(f"Чаще всего встречается буква '{most_frequent_letter}', количество раз: {letter_frequency[most_frequent_letter]}")
