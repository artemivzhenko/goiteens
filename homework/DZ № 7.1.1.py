def spin_words(sentence):
    words = sentence.split()

    result = [word[::-1] if len(word) >= 5 else word for word in words]

    return ' '.join(result)


print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))
