
secret_word = "компост"
hints = [
    f"Длина слова: {len(secret_word)}",
    f"Первая буква: {secret_word[0]}",
    f"Последняя буква: {secret_word[-1]}"
]
for attempt, hint in enumerate(hints, start=1):
    print(f"Подсказка {attempt}: {hint}")
    guess = input("Ваш ответ: ").lower()
    if guess == secret_word:
        print("Правильно!")
        break
else:
    print(f"Вы не угадали! Загаданное слово было: {secret_word}")
