height = 5
for i in range(height, 0, -1):
    print('*' * i)
def get_user():
 hello_message: str = "Hello"
 print(hello_message + " World!")
 user_name: str = input("Please put your name -> \n")
 print(hello_message + " " + user_name)
 user_age_str: str = input("How old are you  -> \n")
 user_age: int = int(user_age_str)
 print(user_name + " is " + str(user_age) +" years old")
 country: str = input("country of user")
 print("user live in " + country)
 person: str = input("hender of user")
 print("user hender is" + person)
 cinema: str = input("favorite cinema of user")
 print("user favorite cinema" + cinema)
 actor: str = input("user favorite actor")
 print("user favorite actor" + actor)
 cinactor: str = input("user favorite film with his favorite actor")
 print("user favorite film and actor" + cinactor)

get_user()
get_user()
