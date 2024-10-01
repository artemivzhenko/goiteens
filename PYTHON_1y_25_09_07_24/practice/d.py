while True:
    user_input=input("Введіть так або ні \n")
    if user_input.lower() in ["так","ні"]:
        break
    else:
        print("Неккоректно введені дані")