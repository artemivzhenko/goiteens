import turtle



screen = turtle.Screen()



def main():
    t = turtle.Turtle()
    t.speed("slow")  

    while True:
        command = input("Введіть команду (вліво, вправо, вперед, назад): ")

        if command == "вліво":
            t.left(90)
            t.forward(50)
        elif command == "вправо":
            t.right(90)
            t.forward(50)
        elif command == "вперед":
            t.forward(50)
        elif command == "назад":
            t.backward(50)
        else:
            print("Невідома команда. Введіть 'вліво', 'вправо', 'вперед' або 'назад'.")

if __name__ == "__main__":
    main()

screen.mainloop()


