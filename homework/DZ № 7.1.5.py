def enumerate_words(sentence):
    words = sentence.split()
    for index, word in enumerate(words, start=1):
        print(f"Порядковый номер: {index}, Слово: {word}")

sentence = "Это пример строки с несколькими словами"
enumerate_words(sentence)
