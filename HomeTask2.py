def get_user():
    hello_message: str = "Hello"
    print(hello_message + " World!")
    #Name
    user_name: str = input("Please put your name -> \n")
    print(hello_message + " " + user_name)
    #Age
    user_age_str: str = input("How old are you? -> \n")
    user_age: float = float(user_age_str)
    print(user_name + " is " + str(user_age) + " years old")
    #Country
    user_country: str = input("In which country do you live? -> \n")
    print(user_name + " live in " + user_country)
    #Heigt
    user_heigt_str: str = input("How tall are you in meters? -> \n")
    user_heigt: float = float(user_heigt_str)
    print(user_name + " is " + str(user_heigt) + " m tall")

get_user()
