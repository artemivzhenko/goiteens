while True:
    name = input("Введите ваше имя: ")
    if name.strip():
        break
    else:
        print("Имя не может быть пустым. Попробуйте еще раз.")

print(f"Привет, {name}!")