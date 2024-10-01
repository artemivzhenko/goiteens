user= input("type your word: ")
user_1=user[::-1]
if user == user_1:
    print(True)
else:
    print(False)