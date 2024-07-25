def get_user():
    hello_message: str = "Hello"
    print(hello_message + " World!")
    user_name: str = input("Please put your name -> \n")
    print(hello_message + " " + user_name)
    user_age_str: str = input("How old are you -> \n")
    user_age: int = int(user_age_str)
    print(user_name + " is " + str(user_age) + " years old")


get_user()
get_user()

# int = Integer
# str = String
# float = Float
