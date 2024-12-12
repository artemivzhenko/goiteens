
users = {}
while True:
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    if username in users:
        print("Такой пользователь уже существует!")
    else:
        users[username] = password
        print("Регистрация прошла успешно!")
    if input("Продолжить? (да/нет): ").lower() != "да":
        break
print(users)
