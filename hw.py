actor: str = input("Who os your favorite actor \n")
print("favorite actor user  " + "is" + actor)
actor: str = input("what is favorite movie where this actor was shot \n")
print("user favorite movie is" + actor)


user_city: str = input("Type the city->")
print(user_city + " is a wonderful place!")




# Висота трикутника
height = 5

# Генерація трикутника
for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * (2 * i - 1))



animal_type = input("Please enter the type of animal: ")
animal_name = input("Please enter the name of the animal: ")
print(f"My favorite {animal_type} is a beautiful animal. Its name is {animal_name}.")