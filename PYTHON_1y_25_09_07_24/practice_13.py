def move_letters(my_string):
    my_list = [ord(i) + 10 for i in my_string]
    my_result = []
    for i in my_list:
        if i <= ord("z"):
            my_result.append(chr(i))
        else:
            my_result.append(chr(i - ord("z") + ord("a")))
    return "".join(my_result)


def move_letters_2(my_string):
    letters = "abcdefghijklmnopqrstuvwxyzabcdefghij"
    return "".join([letters[letters.index(i)+10] for i in my_string])

