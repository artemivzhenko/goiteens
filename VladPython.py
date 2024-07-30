def get_user():
    user_name = input("Введіть своє ім'я -->\n")
    user_subject = input("Введіть ваш улюблений предмет -->\n")
    user_score = int(input("Введіть ваш бал (12/0) -->\n"))
    print("В учня " + user_name + " Улублений предмет " + user_subject + " з балом " + str(user_score))



get_user()