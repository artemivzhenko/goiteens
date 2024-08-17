# написати программу яка запитує у користувача його Імʼя
# і виводить на екран
# а потім запитує його вік і також виводить його на екран


user_name = input("Будь ласка вкажи своє імʼя\n")
# user_name змінна типу String коротка назва str

message = "Імʼя користувача = " + user_name
message += "!!!!!"   # Аналогічна запису    message = message + "!!!!!"
message = user_name * 5

print(message)


user_age: int = 24
# user_age змінна типу Integer коротка назва int
# print(user_age * 5)    # множення
# print(user_age + 45)   # додавання
# print(user_age - 145)  # віднімання
# print(user_age / 65)   # ділення
# print(user_age // 10)  # ціле ділення
# print(user_age % 10)   # отримання остачі
# print(user_age ** 6)   # взведення у степінь

user_number = int(input("Введіть число\n"))
user_number_1 = int(input("Введіть число\n"))
user_number_2 = int(input("Введіть число\n"))
print(user_number)


# user_height: float = 160.8
# user_height змінна типу Float коротка назва float має всі аналогічні операції як і integer


# is_user_male: bool = True
# is_user_male змінна типу Boolean коротка назва bool

print(input("Enter"))
