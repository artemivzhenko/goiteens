def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

user_input = input("Ведіть слово для перевірки на паліндром: ")

if is_palindrome(user_input):
    print(f"Слово '{user_input}' є паліндромом.")
else:
    print(f"Слово '{user_input}' не є паліндромом.")
