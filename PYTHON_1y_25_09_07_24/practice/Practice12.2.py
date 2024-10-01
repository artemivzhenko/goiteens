def anagram_word(str1, str2):
    my_str1 = sorted(str1.lower().replace(" ", ""))
    my_str2 = sorted(str2.lower().replace(" ", ""))

    return my_str1 == my_str2

word1 = input("Введіть перше слово -> \n ")
word2 = input("Введіть друге слово -> \n ")

print(anagram_word(word1,word2))
