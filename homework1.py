def get_user():
    hello_message:  str  = "Hello"
    print(hello_message + " World!")
    user_name: str  = input("Please enter your name -> \n")
    print(hello_message + " " + user_name)
    user_age: int  = input("Please enter your age -> \n")
    print(user_name + " is " + str(user_age) + "years old")
    user_country: str = input("Please enter your country -> \n")
    print(user_name + " is " + str(user_age) + " years old " + " and " +(user_name) + "  live in " + str(user_country))
    user_height: float = input("Please enter your height -> \n")
    print(user_name + " is " + str(user_age) + " years old " + " and " + (user_name) +  " height is " + (user_height) + " cm "  + (user_name) + "  live in " + str(user_country))
get_user()