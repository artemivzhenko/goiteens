string = "Це старий приклад старого рядка."
new_string = string.replace("старий", "новий")
print(new_string)


numbers = [10, 23, 56, 3, 78, 5, 1]
max_value = max(numbers)
min_value = min(numbers)
print("Найбільше значення:", max_value)
print("Найменше значення:", min_value)


numbers = [10, 23, 56, 3, 78, 5, 1]
numbers.reverse()
print("Список у зворотному порядку:", numbers)


favorite_movies = ["Inception", "The Matrix", "Interstellar"]
favorite_movies.append("The Dark Knight")
favorite_movies.remove("Interstellar")
favorite_movies.sort()
print("Улюблені фільми за алфавітом:", favorite_movies)


string = "Hello "
repeated_string = string * 5
print(repeated_string)


original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
copied_list.append(6)
print("Оригінальний список:", original_list)
print("Скопійований та змінений список:", copied_list)


def is_palindrome(word):
    cleaned_word = ''.join(filter(str.isalnum, word)).lower()
    return cleaned_word == cleaned_word[::-1]
word1 = "Madam"
word2 = "Next"
word3 = "Hello olleH"
print(word1, "є паліндромом:", is_palindrome(word1))
print(word2, "є паліндромом:", is_palindrome(word2))
print(word3, "є паліндромом:", is_palindrome(word3))


first_name = "john"
last_name = "doe"
full_name = first_name.capitalize() + " " + last_name.capitalize()
print(full_name)


words = ["Hello", "world", "this", "is", "Python"]
sentence = " ".join(words)
print(sentence)
