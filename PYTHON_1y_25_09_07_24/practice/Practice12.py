def palindrome_word(string):
    my_string = ''.join(string.lower().split())

    return my_string == my_string[::-1]

word = input("Введіть слово -> \n")

print(palindrome_word(word))